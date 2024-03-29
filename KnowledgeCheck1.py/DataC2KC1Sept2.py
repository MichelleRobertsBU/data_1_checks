
import requests as re
import pandas as pd

#Call API
url = "https://api.punkapi.com/v2/beers/1"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(data = r_json)
print(df)
print('')

#Create larger dataframe, choose columns.

beer_list = pd.DataFrame()
url = "https://api.punkapi.com/v2/beers?"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(r_json)
selection = df[["name", "abv", "tagline",]]
beer_list = pd.concat([beer_list, selection])
print(beer_list)
print('')

#Write a query in Pandas to select a particular set of your data.

beer_abv = beer_list.query("abv > 5.0")
print(beer_abv)
print('')


#Determine beer with lowest and highest abv (alcohol by volume)

url = "https://api.punkapi.com/v2/beers?"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(r_json)
df_abv = df[["name","abv"]]
df_low = df_abv["abv"].min()
df_high = df_abv["abv"].max()
print('')
print("The beer with the lowest alcohol by volume is")
print(df_abv.loc[df_abv["abv"]==df_abv["abv"].min(),:])
print('')
print("The beer with the highest alcohol by volume is")
print(df_abv.loc[df_abv["abv"]==df_abv["abv"].max(),:])
print('')


#Select and print the SECOND AND THIRD columns of your data frame

url = "https://api.punkapi.com/v2/beers?page=2&per_page=80"
r = re.get(url)
r_json = r.json()
df_large = pd.json_normalize(data = r_json)
print(df_large.keys())
print('')
print(df_large[["name", "tagline"]])
print('')

#Select and print the FIRST 4 rows of your data frame
print(df_large.iloc[:4])

    







