"""Clean monthly precipitation data for five countries for 2000–2025.

Read raw Excel files from country folders under data/raw/ for Brazil,
Vietnam, Colombia, Indonesia, and Ethiopia. Keep selected coffee-growing
regions and reshape the data into one row per region and year, with
January–December columns. Add country names and save a cleaned Excel
file for each country in data/clean/per/.
"""

#1 Brazil

import pandas as pd 

df = pd.read_excel("data/raw/Brazil/per_Brazil.xlsx")

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

coffee_producing_regions = df_cleaned["name"] == "Minas Gerais"
df_cleaned = df_cleaned[coffee_producing_regions]

monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()


df_cleaned.insert(0, "country", "Brazil")

df_cleaned.to_excel("data/clean/per/Brazil_per.xlsx", index=False,) 


#2 Vietnam

df = pd.read_excel("data/raw/Vietnam/per_Vietnam.xlsx")

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

coffee_producing_regions = df_cleaned["name"].isin(["Dac Lac", "Gia Lai", "Dac Nong", "Lam Dong", "Kon Tum"])
df_cleaned = df_cleaned[coffee_producing_regions]

monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 

df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

df_cleaned.insert(0, "country", "Vietnam")

df_cleaned.to_excel("data/clean/per/Vietnam_per.xlsx", index=False,) 



#3 Colombia


df = pd.read_excel("data/raw/Colombia/per_Colombia.xlsx")

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

coffee_producing_regions = df_cleaned["name"].isin(["Caldas", "Quindio", "Risaralda", "Huila", "Cauca", "Nariño"])
df_cleaned = df_cleaned[coffee_producing_regions]

monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 

df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)

df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

df_cleaned.insert(0, "country", "Colombia")

df_cleaned.to_excel("data/clean/per/Colombia_per.xlsx", index=False,) 


#4 Indonesia

df = pd.read_excel("data/raw/Indonesia/per_Indonesia.xlsx")

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

coffee_producing_regions = df_cleaned["name"].isin(["Sumatera Selatan", "Lampung", "Sumatera Utara", "Nangroe Aceh Darussalam", "Bengkulu"])
df_cleaned = df_cleaned[coffee_producing_regions]

monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 

df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)

df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

df_cleaned.insert(0, "country", "Indonesia")

df_cleaned.to_excel("data/clean/per/Indonesia_per.xlsx", index=False,) 



#5 Ethiopia

df = pd.read_excel("data/raw/Ethiopia/per_Ethiopia.xlsx")


drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

coffee_producing_regions = df_cleaned["name"].isin(["Oromia", "SNNP", "Sidama"])
df_cleaned = df_cleaned[coffee_producing_regions]

monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 

df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)

df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

df_cleaned.insert(0, "country", "Ethiopia")

df_cleaned.to_excel("data/clean/per/Ethiopia_per.xlsx", index=False,) 

























