"""Combine cleaned temperature data for five countries.

Read country Excel files from data/clean/temp/, remove geographic codes,
sort by country, region, and year, and calculate mean monthly temperature
for each region-year. Save to data/clean/temperature_combined.csv."""

import pandas as pd 


brazil = pd.read_excel("data/clean/temp/Brazil_temp.xlsx")
vietnam = pd.read_excel("data/clean/temp/Vietnam_temp.xlsx")
colombia = pd.read_excel("data/clean/temp/Colombia_temp.xlsx")
indonesia = pd.read_excel("data/clean/temp/Indonesia_temp.xlsx")
ethiopia = pd.read_excel("data/clean/temp/Ethiopia_temp.xlsx")


combined= pd.concat([brazil, vietnam, colombia, indonesia, ethiopia], ignore_index=True,)


combined = combined.drop(columns=["code"])

combined = combined.sort_values(["country", "name", "Year"])

combined["Annual_Average_Temperature"] = combined.loc[:, "Jan":"Dec"].mean(axis=1)


combined.to_csv("data/clean/temperature_combined.csv", index=False, encoding="utf-8-sig") 
