import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')


df = df[['Adj. Close']]
print(df.head())

forecast_col = 'Adj. close'
df.fillna(-9999,inplace=True)
