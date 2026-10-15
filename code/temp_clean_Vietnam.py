""" Clean monthly temperature data for selected Vietnamese regions, 2000–2025.

Read data/raw/Vietnam/tas_Vietnam.xlsx and save one row per region and
year, with January–December columns, to data/clean/temp/Vietnam_temp.xlsx """

import pandas as pd 
df = pd.read_excel("data/raw/Vietnam/tas_Vietnam.xlsx")


drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)


coffee_producing_regions = df_cleaned["name"].isin(["Dac Lac", "Gia Lai", "Dac Nong", "Lam Dong", "Kon Tum"])
df_cleaned = df_cleaned[coffee_producing_regions]


monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Average Surface Air Temperature")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Average Surface Air Temperature",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

df_cleaned.insert(0, "country", "Vietnam")

df_cleaned.to_excel("data/clean/temp/Vietnam_temp.xlsx", index=False,) 
