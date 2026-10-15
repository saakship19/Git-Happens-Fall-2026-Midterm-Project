"""Combine cleaned precipitation data for five countries.
Read country Excel files from data/clean/per/, remove geographic codes, sort by country
region and year. Then. calculate average monthly precipitation for each region-year. Save the combined
dataset to data/clean/precipitation_combined.csv"""

import pandas as pd 


brazil = pd.read_excel("data/clean/per/Brazil_per.xlsx")
vietnam = pd.read_excel("data/clean/per/Vietnam_per.xlsx")
colombia = pd.read_excel("data/clean/per/Colombia_per.xlsx")
indonesia = pd.read_excel("data/clean/per/Indonesia_per.xlsx")
ethiopia = pd.read_excel("data/clean/per/Ethiopia_per.xlsx")


combined= pd.concat([brazil, vietnam, colombia, indonesia, ethiopia], ignore_index=True,)


combined = combined.drop(columns=["code"])

combined = combined.sort_values(["country", "name", "Year"])

combined["Average_Precipitation"] = combined.loc[:, "Jan":"Dec"].mean(axis=1)


combined.to_csv("data/clean/precipitation_combined.csv", index=False, encoding="utf-8-sig") 
