import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('assets\california_housing_test.csv')
df.head()
print(df)

df.plot(kind = 'hist', x = 'housing_median_age', y = 'median_house_value')
plt.xlabel('Housing Median Age')
plt.ylabel('Median House Value')

plt.show()
