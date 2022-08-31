from importlib.resources import path
import pandas as pd
import os

csv_data_mean = pd.read_csv("Temperature_And_Precipitation_Cities_IN/Bangalore_1990_2022_BangaloreCity.csv")
csv_data_median = csv_data_mean

print(csv_data_mean.head())

print("Cleaned by mean")
csv_data_mean[['tavg','tmin','tmax']]=csv_data_mean[['tavg','tmin','tmax']].fillna(csv_data_mean.mean())
csv_data_mean[['prcp']]=csv_data_mean[['prcp']].fillna(0)
print(csv_data_mean.head())

print("Cleaned by median")
csv_data_median[['tavg','tmin','tmax']]=csv_data_median[['tavg','tmin','tmax']].fillna(csv_data_median.median())
csv_data_median[['prcp']]=csv_data_median[['prcp']].fillna(0)
print(csv_data_median.head())

os.makedirs('Output', exist_ok=True)
csv_data_mean.to_csv('Output/Bangalore_1990_2022_BangaloreCity_mean.csv',index=False)  
csv_data_median.to_csv('Output/Bangalore_1990_2022_BangaloreCity_median.csv',index=False)