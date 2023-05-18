import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# The Bitcoin halving dates
halving_dates = ['2015-08-25', '2019-08-05', '2023-08-03']
# halving_dates = ['2016-07-09', '2020-05-11']
#'2012-11-28'

# Days before and after halving to consider
days_before = 200
days_after = 100

# Download historical market data
btc = yf.Ticker("LTC-USD")
# btc = yf.Ticker("BTC-USD")

plt.figure(figsize=(10, 5))

for i, date in enumerate(halving_dates):
    start_date = (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=days_before)).strftime('%Y-%m-%d')
    end_date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=days_after)).strftime('%Y-%m-%d')

    
    hist = btc.history(start=start_date, end=end_date)

    # Generate a series of integers to represent each date on the X axis
    x = list(range(-days_before, days_after))

    # Ensure y has the same length as x
    y = np.empty(len(x))
    y.fill(np.nan)  # initially fill y with NaN values


    # Normalize data to start from the halving date price
    # normalized_prices = hist["Close"] / hist["Close"].loc[date]

     # Calculate price return percentage
    initial_price = hist["Close"].iloc[0]
    return_percentage = (hist["Close"] - initial_price) / initial_price * 100

    # Update y values with the actual return_percentage for available data points
    y[:len(return_percentage)] = return_percentage


    plt.plot(x, y, label='Halving ' + str(i + 1))



plt.legend()
plt.grid()
plt.title("Litecoin Price Relative to Halving Dates")
plt.xlabel("Days Relative to Halving Date")
plt.ylabel("Return %")
plt.savefig('ltc_halvings.png')
