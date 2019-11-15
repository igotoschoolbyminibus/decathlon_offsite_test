Q3:

  In order to forecast the monthly turnover, ARIMA model has been adapted as the prediction model. In ARIMA model, it can be divided into 3 parts, respectively Autoregressive model (p), Differencing (d) and Moving Average (q). 
  
  For Autoregressive Model, it means the future turnover is determined by past p lags values. For Moving Average, it indicates the regression error is a linear combination of previous q lags. d indicates the degree of differencing which is used to elinimate the non-stationarity of the time series. To sum up, ARIMA model is built by past p lag values, regression error of previous q lags, and the difference between lags.
  
  To apply ARIMA model, we first need to check the stationarity of the time series of 4 stores, this time Adfuller test is used to test the stationarity of the time series. If the p-value of the test is less than 0.05, then we would say there is a significant evidenct to say a time series is stationarity. The result reveal that all stores except store 2350 are stationary time series. For store 2350, I try to perform log-transform and perform the test again, and the p-value has been improved a lot (although it is still not significant enough to prove stationarity). So log values will be used as training data for ARIMA model for store 2350.
  
  The next step is to determine the value of p, d and q. This time, p set to 7 to indicate the turnover trend across the week, but for store 191, it returns error when p=7, so I use p=30 instead to predict the turnover by linear combination of past 30 days. For d, i set d=1 for store 191, 1614 and 1618 to further elinimate the non-stationarity by first degree differencing, d is set to 0 for store 2350 since is has become stationary by performing log transformation. For q, we use Partial Autocorrelation Function to determine the value,
since from all graphs we can see there is a sharp dropoff on PACF when q = 1 & q = 2, so we choose q = 3 for all stores.

  After selecting the parameter, the model can be run to predict the daily turnover of each store up to the end of 2020.\
  
  For the result, we found that the store 1614 and 2350 shows an decreasing trend on the forecasting, one of the reason would the social unrest starting from June affects the willingness for customers to buy things. On the other hand, i guess there is some campgian held on store 2350 on its recently openings which also affects the prediction. Further in-depth analysis need to be made to assess the impact of factors mentioned above.
  
Q5:
  
-> Determine Independent Variables:
	--> ttl_txn_off
	--> avg_qty_per_txn_off
	--> avg_to_per_qty_off
	Purpose: Figure out the offline shopping behavior of a customer
	--> ttl_txn_on
	--> avg_qty_per_txn_on
	--> avg_to_per_qty_on
	Purpose: Figure out the online shopping behavior of a customer
	--> to_share_online
	Purpose: Figure out the if a customer favour online or offline shopping
	--> to_share_gender_gap
	--> to_share_kid
	Purpose: Figure out the demand distribution of each customer
	--> to_share_weekday
	--> to_share_weekend
	Purpose: Figure out the time slot that customer favour to shop

	Other Considerations:
		> The following variable is treated as dependent variable (The outcome based on customer behavior)
			>> Categories
		> Same column with high correlation is removed
			>> e.g. Total (Online + Office) Figures
		> Age is not used as independent variable because the information is not complete (only 20% of records with age)

-> Preprocessing
	--> Remove outliers (Top 5 person)
		> Too extreme to affect the k-means clustering result (k-means result is easily affected by outliers)
	--> Elbow method to determine k (no of clusters)
		> Elbow appears when k=3 and k=7, but the clusters is not clear when k=3, so use k=7 instead (and the clusters are quite clear)

-> Analysis:
	--> Group 0: Offline buyers who likely to shop during holiday / weekend
		> Avg turnover per transaction: $275
		> Avg turnover per item: $96
		> Avg item per transaction: 3.07
		> Total Transaction: 2.95
		> Popular categories: Hiking, Jogging, Swimming, Trekking (Aerobic Exercise)
	--> Group 1: Offline buyers who likely to shop during weekday
		> Avg turnover per transaction: $236
		> Avg turnover per item: $94
		> Avg item per transaction: 2.59
		> Total Transaction: 2.83
		> Popular categories: Hiking, Jogging, Swimming, Trekking 
		> Compared to group 0, group 1 customer has less item per transaction
	--> Group 2: Offline buyer with high frequency to come back
		> Avg turnover per transaction: $225
		> Avg turnover per item: $82
		> Avg item per transaction: 2.78
		> Total Transaction: 15.13
		> Popular categories: Hiking, Jogging, Swimming, Trekking
		> Average age = 41.5, which is slightly higher than average (around 39)
		> Among group 2, 28% of them also enjoyed online shopping, compared to 5% for both group 0 & 1
		> Average Men, Women, Kid Ratio (43.68%, 27.57%, 27.80%)
		> More likely to purchase on weekday (63.69%), but sometimes weekend (36.31%) & holiday (41.21%)
	--> Group 3: Online buyer who are likely to shop during weekday with higher single time purchase amount 
		> Avg turnover per transaction: $525
		> Avg turnover per item: $170
		> Avg item per transaction: 4.41
		> Total Transaction: 7.7
		> Popular categories: Body Building, Hiking
		> Average age = 36.2, which is slightly lower than average (around 39)
		> 36% of them also enjoyed offline shopping
		> Average Men, Women, Kid Ratio (22.95%, 14.78%, 19.99%)
	--> Group 4: Online buyer with very large quantities
		> Avg turnover per transaction: $11,280
		> Avg turnover per item: $46
		> Avg item per transaction: 216.05
		> Total Transaction: 1.18
		> Popular categories: Tennis, Hiking, Swimming 
		> High Ratio for kids: 30.49% compared to Men (0.88%) and Women (4.99%)
		> Similar Ratio between weekday (58.2%) and weekend (41.8%)
		> The group probably represents some sports club which will open classes for kids
	--> Group 5: Online buyer who are likely to purchase during weekend
		> Avg turnover per transaction: $855
		> Avg turnover per item: $565
		> Avg item per transaction: 2.35
		> Total Transaction: 1.14
		> Popular categories: Body Building, Fitness, Hiking
		> Not frequent buyer, but they tends to purchase products will higher price
		> 32% of them also tried buying offline
		> Similar Ratio between Men (16.32%), Women (11.83%), and Kid (19.26%)
		> Average age = 37.5
	--> Group 6: Offline buyer who are likely to purchase kids items
		> Avg turnover per transaction: $347
		> Avg turnover per item: $89
		> Avg item per transaction: 4.16
		> Total Transaction: 3.59
		> Popular categories: Football, Hiking, Surfing, Swimming, Tennis

-> Insights
	--> Hiking is popular among all groups
	--> For online buyers, some of them also tried offline shopping, maybe its good to see their overall customer journey.
	--> Online transactions tends to be either large in quantity or high in single price
