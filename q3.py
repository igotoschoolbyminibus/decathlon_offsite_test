# Import Package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from matplotlib import pyplot
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf

# Import Data
data = pd.read_csv('q3.csv')

# Try use daily figures
daily_store_data = data.groupby(['store', 'date']).sum()
daily_store_data = daily_store_data.reset_index()
daily_turnover_data = daily_store_data.pivot(index='date', columns='store', values='turnover')
daily_turnover_data = daily_turnover_data.reset_index()
plt.plot(daily_turnover_data['date'], daily_turnover_data[191], color='blue')
plt.show()
plt.plot(daily_turnover_data['date'], daily_turnover_data[1614], color='red')
plt.plot(daily_turnover_data['date'], daily_turnover_data[1618], color='yellow')
plt.plot(daily_turnover_data['date'], daily_turnover_data[2350], color='green')

# Test if the time series is stationary
## 191
test_191 = daily_turnover_data[191]
result = adfuller(test_191)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
    
## 1614
test_1614 = daily_turnover_data[1614].dropna()
result = adfuller(test_1614)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
    
## 1618
test_1618 = daily_turnover_data[1618].dropna()
result = adfuller(test_1618)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

## 2350
test_2350 = daily_turnover_data[2350][683:]
test_2350 = np.log(test_2350.replace([np.inf, -np.inf], np.nan)).replace([np.inf, -np.inf], np.nan).dropna()
last_value_2350 = test_2350.iloc[-1]
test_2350 = (test_2350 - test_2350.shift(1)).dropna()
result = adfuller(test_2350)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
    
# Determine the parameters
## 191
autocorrelation_plot(test_191)
plot_pacf(test_191, lags=30)
## 1614
autocorrelation_plot(test_1614)
plot_pacf(test_1614, lags=30)
## 1618
autocorrelation_plot(test_1618)
plot_pacf(test_1618, lags=30)
## 2350
autocorrelation_plot(test_2350)
plot_pacf(test_2350, lags=30)

# Build Model
predictions = list()
## 191
model_191 = ARIMA(list(test_191), order=(30,1,3))
model_fit_191 = model_191.fit(disp=False)
print(model_fit_191.summary())
## 1614
model_1614 = ARIMA(list(test_1614), order=(7,1,3))
model_fit_1614 = model_1614.fit(disp=False)
print(model_fit_1614.summary())
## 1618
model_1618 = ARIMA(list(test_1618), order=(7,1,3))
model_fit_1618 = model_1618.fit(disp=False)
print(model_fit_1618.summary())
## 2350
model_2350 = ARIMA(list(test_2350), order=(7,0,3))
model_fit_2350 = model_2350.fit(disp=False)
print(model_fit_2350.summary())

# Forecast
## Prepare a list with year month
corr_year_month = list()
year_month_201911 = np.array(201911)
corr_year_month.extend(np.repeat(year_month_201911, 30))
year_month_201912 = np.array(201912)
corr_year_month.extend(np.repeat(year_month_201912, 31))
year_month_202001 = np.array(202001)
corr_year_month.extend(np.repeat(year_month_202001, 31))
year_month_202002 = np.array(202002)
corr_year_month.extend(np.repeat(year_month_202002, 29))
year_month_202003 = np.array(202003)
corr_year_month.extend(np.repeat(year_month_202003, 31))
year_month_202004 = np.array(202004)
corr_year_month.extend(np.repeat(year_month_202004, 30))
year_month_202005 = np.array(202005)
corr_year_month.extend(np.repeat(year_month_202005, 31))
year_month_202006 = np.array(202006)
corr_year_month.extend(np.repeat(year_month_202006, 30))
year_month_202007 = np.array(202007)
corr_year_month.extend(np.repeat(year_month_202007, 31))
year_month_202008 = np.array(202008)
corr_year_month.extend(np.repeat(year_month_202008, 31))
year_month_202009 = np.array(202009)
corr_year_month.extend(np.repeat(year_month_202009, 30))
year_month_202010 = np.array(202010)
corr_year_month.extend(np.repeat(year_month_202010, 31))
year_month_202011 = np.array(202011)
corr_year_month.extend(np.repeat(year_month_202011, 30))
year_month_202012 = np.array(202012)
corr_year_month.extend(np.repeat(year_month_202012, 31))
corr_year_month_array = np.asarray(corr_year_month)

# Fit Model
yhat_191 = model_fit_191.forecast(steps=427)[0]
prediction_daily_191 = pd.DataFrame({'predicted_revenue':yhat_191, 'year_month':corr_year_month_array})
prediction_month_191 = prediction_daily_191.groupby(['year_month']).sum()

yhat_1614 = model_fit_1614.forecast(steps=427)[0]
prediction_daily_1614 = pd.DataFrame({'predicted_revenue':yhat_1614, 'year_month':corr_year_month_array})
prediction_month_1614 = prediction_daily_1614.groupby(['year_month']).sum()

yhat_1618 = model_fit_1618.forecast(steps=427)[0]
prediction_daily_1618 = pd.DataFrame({'predicted_revenue':yhat_1618, 'year_month':corr_year_month_array})
prediction_month_1618 = prediction_daily_1618.groupby(['year_month']).sum()

yhat_2350 = model_fit_2350.forecast(steps=427)[0]
yhat_2350 = pd.Series(yhat_2350)
yhat_2350 = yhat_2350 + yhat_2350.shift(1)
yhat_2350[0] = model_fit_2350.forecast(steps=427)[0][0] + last_value_2350
for i in range(1,len(yhat_2350)):
    yhat_2350[i] = yhat_2350[i-1] + yhat_2350[i]
yhat_2350 = np.exp(yhat_2350)
prediction_daily_2350 = pd.DataFrame({'predicted_revenue':yhat_2350, 'year_month':corr_year_month_array})
prediction_month_2350 = prediction_daily_2350.groupby(['year_month']).sum()
