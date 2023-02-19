
import requests as re
import pandas as pd

#Call API
url = "https://api.punkapi.com/v2/beers/1"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(data = r_json)
print(df)

#Create larger dataframe, choose columns
beer_list = pd.DataFrame()
url = "https://api.punkapi.com/v2/beers?"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(r_json)
selection = df[["name", "abv", "tagline",]]
beer_list = pd.concat([beer_list, selection])
print(beer_list)

#Determine beer with lowest and highest abv (alcohol by volume)

url = "https://api.punkapi.com/v2/beers?"
r = re.get(url)
r_json = r.json()
df = pd.json_normalize(r_json)
df_abv = df[["name","abv"]]
df_low = df_abv["abv"].min()
df_high = df_abv["abv"].max()
print("The beer with the lowest alcohol by volume is")
print(df_abv.loc[df_abv["abv"]==df_abv["abv"].min(),:])
print("The beer with the highest alcohol by volume is")
print(df_abv.loc[df_abv["abv"]==df_abv["abv"].max(),:])

#



    






