Q3:

  In order to forecast the monthly turnover, ARIMA model has been adapted as the prediction model. In ARIMA model, it can be divided into 3 parts, respectively Autoregressive model (p), Differencing (d) and Moving Average (q). 
  
  For Autoregressive Model, it means the future turnover is determined by past p lags values. For Moving Average, it indicates the regression error is a linear combination of previous q lags. d indicates the degree of differencing which is used to elinimate the non-stationarity of the time series. To sum up, ARIMA model is built by past p lag values, regression error of previous q lags, and the difference between lags.
  
  To apply ARIMA model, we first need to check the stationarity of the time series of 4 stores, this time Adfuller test is used to test the stationarity of the time series. If the p-value of the test is less than 0.05, then we would say there is a significant evidenct to say a time series is stationarity. The result reveal that all stores except store 2350 are stationary time series. For store 2350, I try to perform log-transform and perform the test again, and the p-value has been improved a lot (although it is still not significant enough to prove stationarity). So log values will be used as training data for ARIMA model for store 2350.
  
  The next step is to determine the value of p, d and q. This time, p set to 7 to indicate the turnover trend across the week, but for store 191, it returns error when p=7, so I use p=30 instead to predict the turnover by linear combination of past 30 days. For d, i set d=1 for store 191, 1614 and 1618 to further elinimate the non-stationarity by first degree differencing, d is set to 0 for store 2350 since is has become stationary by performing log transformation. For q, we use Partial Autocorrelation Function to determine the value,
since from all graphs we can see there is a sharp dropoff on PACF when q = 1 & q = 2, so we choose q = 3 for all stores.

  After selecting the parameter, the model can be run to predict the daily turnover of each store up to the end of 2020.\
  
  For the result, we found that the store 1614 and 2350 shows an decreasing trend on the forecasting, one of the reason would the social unrest starting from June affects the willingness for customers to buy things. On the other hand, i guess there is some campgian held on store 2350 on its recently openings which also affects the prediction. Further in-depth analysis need to be made to assess the impact of factors mentioned above.
  
Q5:
  
