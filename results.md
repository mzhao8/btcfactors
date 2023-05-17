                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.044
Model:                            OLS   Adj. R-squared:                  0.044
Method:                 Least Squares   F-statistic:                     123.7
Date:                Tue, 16 May 2023   Prob (F-statistic):           4.06e-28
Time:                        17:24:54   Log-Likelihood:                -29876.
No. Observations:                2692   AIC:                         5.976e+04
Df Residuals:                    2690   BIC:                         5.977e+04
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                  1.778e+04    362.511     49.048      0.000    1.71e+04    1.85e+04
negative_miner_change     0.7456      0.067     11.120      0.000       0.614       0.877
==============================================================================
Omnibus:                      444.191   Durbin-Watson:                   0.006
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              690.533
Skew:                           1.220   Prob(JB):                    1.13e-150
Kurtosis:                       3.453   Cond. No.                     6.36e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.36e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

Interpretation:

Dep. Variable: This is the dependent variable, or the variable you're trying to predict. In your case, it's 'price'.

Model: This is the statistical model that was used, which in this case is OLS.

Method: This is the method used to fit the data to the model, which in this case is 'Least Squares'.

No. Observations: This is the number of observations, or data points, used in the regression analysis. Here, it's 2692.

Df Residuals and Df Model: These represent the degrees of freedom of the residuals and the model respectively. The degrees of freedom of the residuals is the number of observations minus the number of parameters. The degrees of freedom of the model is the number of predictors in the model (in this case, 1: negative_miner_change).

coef: These are the coefficients of the regression equation. In your case, the equation would be price = 1.778e+04 + 0.7456*negative_miner_change. This means that for each unit decrease in negative_miner_change, the price is predicted to increase by approximately 0.7456 units.

std err: These are the standard errors of the coefficients. The standard error is a measure of the variability in the estimate for the coefficient.

t: These are the t-statistics for the hypothesis test that each coefficient is different from zero. The larger the t-statistic, the stronger the evidence that there is a significant relationship between the feature and the target.

P>|t|: These are the p-values associated with the t-statistics. If a p-value is less than your chosen significance level (often 0.05), you can reject the null hypothesis that the coefficient is zero. In this case, both p-values are less than 0.05, which indicates that both coefficients are statistically significant.

[0.025 0.975]: These are the 95% confidence intervals for the coefficients. If the confidence interval for a coefficient does not include zero, that indicates that the coefficient is statistically significant at the 5% level.

R-squared: This is the coefficient of determination, which is a statistical measure of how well the regression line approximates the real data points. An R-squared of 100% indicates that all changes in the dependent variable are completely explained by changes in the independent variable(s). In this case, the R-squared value is 0.044, indicating that only about 4.4% of the variation in the price can be explained by the negative_miner_change.

Adj. R-squared: This is the adjusted R-squared, which adjusts the statistic based on the number of independent variables in the model. It's especially useful when comparing the fit of models with a different number of variables.

F-statistic: This is the F-statistic for a joint hypothesis that all coefficients (excluding the intercept) are zero. The larger the F-statistic, the stronger the evidence against this joint hypothesis.

Prob (F-statistic): This is the p-value associated with the F-statistic. If this p-value is less than your chosen significance level, you can reject the null hypothesis that all coefficients (excluding the intercept) are zero.