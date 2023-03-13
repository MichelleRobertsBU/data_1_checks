import pandas as pd
import numpy as np

df = pd.read_csv('assets\Louisville_Metro_KY_-_Fire_Property_Damage (1).csv')
pd.set_option('display.max_columns', None)

print(df.iloc[:3])
print(df.columns)

#Rename columns
df.rename(columns={df.columns[0]: 'Incident Number', df.columns[1]: 'Incident Date', df.columns[3]: 'Incident Type', df.columns[4]: 'Content Loss', df.columns[5]: 'Property Loss', df.columns[6]: 'Total Loss', df.columns[7]: 'Pre-Incident Value'},inplace=True)
print(df.columns)

#Replace null values with 0
newdf = df.fillna(0)
print(newdf.iloc[:10])
