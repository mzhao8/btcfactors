import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# utility function to filter by the date
def filter_by_date(df, date_column, start_date, end_date):
    df[date_column] = pd.to_datetime(
        df[date_column])  # Convert the date column to datetime
    mask = (df[date_column] >= start_date) & (
        df[date_column] <= end_date
    )  # Create a boolean mask for the date range
    return df.loc[mask]  # Return the filtered dataframe

# takes in the btc_metrics csv
df = pd.read_csv('btc_metrics.csv')

# Filter for the date
df = filter_by_date(df, 'date', '2016-01-01', '2023-05-01')

# Price % change
df['price_pct_change'] = df['price'].pct_change()
# To convert it to percentage, you can multiply by 100
df['price_pct_change'] = df['price_pct_change'] * 100

# change in miners absolute
df['miner_change'] = df['miner_balance'].diff()

# Change in miners relative to spot volume of that date (in a percentage format)
df['relative_miner_change_to_spot_vol'] = df['miner_change'] * df[
    'price'] / df['spot_vol_1d'] * 100

# FILTER OUT TO INCLUDE ONLY NEGATIVE NUMBERS; assuming that only when they sell, it affects
df = df[df['miner_change'] < 0]

# FILTER OUT FOR ONLY LARGE % CHANGES (only when the amount sold is greater than 1% of total spot volume that day)
df = df[df['relative_miner_change_to_spot_vol'].abs() > 1]

# remove the first row with NaN
df = df.dropna()

# save to CSV
df.to_csv("btc_metrics_edited.csv")

# Define the dependent variable (log_price) and the independent variable (negative_miner_change)
Y = df['price_pct_change']
X = df['relative_miner_change_to_spot_vol']
X = sm.add_constant(
    X)  # Add a constant term to the predictor (the y-intercept)

# Create a model
model = sm.OLS(Y, X)

# Fit the model to the data
results = model.fit()

# Print out the results
print(results.summary())

# Generate the values for the regression line
line_x = np.linspace(df['relative_miner_change_to_spot_vol'].min(),
                     df['relative_miner_change_to_spot_vol'].max(), 100)
line_y = results.params[0] + results.params[1] * line_x

# Create a scatter plot of the original data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(df['relative_miner_change_to_spot_vol'],
            df['price_pct_change'],
            label='Data')
plt.plot(line_x, line_y, color='red', label='Regression Line')

# Add title and labels
plt.title('Price % Change vs Miner Relative Position Change to Spot Vol')
plt.xlabel('% miner change to spot volume')
plt.ylabel('% price change')
plt.legend()

# Show the plot
plt.show()
