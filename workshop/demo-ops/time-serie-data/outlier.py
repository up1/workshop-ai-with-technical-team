import pandas as pd
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("data.csv")
print("Input data")
print(df.head)
df.columns=["ds","y"]
# If you need to convert data
#df["ds"] =  pd.to_datetime(df["ds"],utc=False,unit='s')
#df['ds'] = pd.to_datetime(df.ds)
print(df.head)

m = Prophet(changepoint_prior_scale=0.05,changepoint_range=1,interval_width=.95)
m.fit(df)

# we are not concerned about predicting here, rather just fitting the data
future = m.make_future_dataframe(periods =2,freq='2h') 
print(" -- make_future_dataframe-- ")
print(future.tail())


forecast = m.predict(future)
print(" -- model predict-- ")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

fig = m.plot(forecast)
fig.savefig('forecastwiki.png')

#Lets identify the points that are over the threshold

 # find the dataframes having same indices
forecast_truncated_index =forecast.index.intersection(df.index)
forecast_truncated = forecast.loc[forecast_truncated_index]
print(forecast_truncated.shape[0],df.shape[0])

# Identify the thresholds 
#indices =m.history[m.history['y'] > forecast_truncated['yhat_upper'] + buffer].index

# Identify the thresholds with some buffer
buffer = np.max( forecast_truncated['yhat_upper'])
print("Buffer=",buffer)
indices =m.history[m.history['y'] > buffer].index

# Get those points that have crossed the threshold
thresholded_df  = m.history.iloc[indices] # ------> This has the thresholded values and more important timestamp

figsize=(10, 6)
fig = plt.figure(facecolor='w', figsize=figsize)
ax = fig.add_subplot(111)
fig = m.plot(forecast,ax=ax)

# plot the thresholded points as red
import warnings
warnings.simplefilter("ignore", category=FutureWarning)
# your plotly code
ax.plot(np.array(thresholded_df['ds'].dt.to_pydatetime()), thresholded_df['y'], 'r.',
        label='Thresholded data points')
fig.savefig('forecastwiki_thresholded.png')