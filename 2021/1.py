import pandas as pd

inputfilename = '1-input.csv'

df = pd.read_csv(inputfilename, header=None, names=['measure'])

df1 = df.copy()
df1['prev'] = df.shift()
df1['diff'] = df1['measure'] - df1['prev']
df1['increase'] = df1['diff'] > 0
df1['increase'].value_counts()

df2 = df.copy()
df2['rolling_3'] = df2.rolling(3).sum()
df2['prev'] = df2['rolling_3'].shift()
df2['rolling_3_increase'] = df2['rolling_3'] > df2['prev']
df2['rolling_3_increase'].value_counts()
