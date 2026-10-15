#Cleaning the rainfall datasets

###### 1 Brazil 

import pandas as pd 

df = pd.read_excel("data/raw/Brazil/per_Brazil.xlsx")


#I want to drop columns that are not useful to me

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

# Now I want to keep just the coffee producing region 
coffee_producing_regions = df_cleaned["name"] == "Minas Gerais"
df_cleaned = df_cleaned[coffee_producing_regions]

# Now I want to create columns for each month to re-arrange my data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()


# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Brazil")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/per/Brazil_per.xlsx", index=False,) 


##### 2 Vietnam 

df = pd.read_excel("data/raw/Vietnam/per_Vietnam.xlsx")

#Drop columns we do not want 

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)


#Keep only the regions I want 
coffee_producing_regions = df_cleaned["name"].isin(["Dac Lac", "Gia Lai", "Dac Nong", "Lam Dong", "Kon Tum"])
df_cleaned = df_cleaned[coffee_producing_regions]

# Creating columns to re-arrange data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Vietnam")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/per/Vietnam_per.xlsx", index=False,) 



#### 3 Colombia 


df = pd.read_excel("data/raw/Colombia/per_Colombia.xlsx")

#Drop columns we do not want 

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

#Keep only the regions I want 
coffee_producing_regions = df_cleaned["name"].isin(["Caldas", "Quindio", "Risaralda", "Huila", "Cauca", "Narino"])
df_cleaned = df_cleaned[coffee_producing_regions]

# Creating columns to re-arrange data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Colombia")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/per/Colombia_per.xlsx", index=False,) 


### 4 Indonesia 

df = pd.read_excel("data/raw/Indonesia/per_Indonesia.xlsx")

#Drop columns we do not want 

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

#Keep only the regions I want 
coffee_producing_regions = df_cleaned["name"].isin(["Sumatera Selatan", "Lampung", "Sumatera Utara", "Nangroe Aceh Darussalam", "Bengkulu"])
df_cleaned = df_cleaned[coffee_producing_regions]

# Creating columns to re-arrange data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Indonesia")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/per/Indonesia_per.xlsx", index=False,) 



### 5 Ethiopia 

df = pd.read_excel("data/raw/Ethiopia/per_Ethiopia.xlsx")

#Drop columns we do not want 

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

#Keep only the regions I want 
coffee_producing_regions = df_cleaned["name"].isin(["Oromia", "SNNP", "Sidama"])
df_cleaned = df_cleaned[coffee_producing_regions]

# Creating columns to re-arrange data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Precipitation")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Precipitation",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()

# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Ethiopia")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/per/Ethiopia_per.xlsx", index=False,) 

























