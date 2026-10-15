#All country temperature files cleaning 

#Brazil 

# first we will clean the Brazil temeprature excel, right now there is data from 1902 but we only need it from 2000

import pandas as pd 

df = pd.read_excel("data/raw/Brazil/tas_Brazil.xlsx")


#I want to drop columns that are not useful to me

drop_columns = df.loc[:, "1901-01":"1999-12"].columns 
df_cleaned = df.drop (columns = drop_columns)

# Now I want to keep just the coffee producing region 
coffee_producing_regions = df_cleaned["name"] == "Minas Gerais"
df_cleaned = df_cleaned[coffee_producing_regions]

# Now I want to create columns for each month to re-arrange my data 

#Turn year into rows 
monthly_data = df_cleaned.melt( id_vars=["code","name"], var_name= "year", value_name= "Average Surface Air Temperature")

#Seperate Dates into Year and Months 
monthly_data ["year"] = pd.to_datetime(monthly_data["year"], format= "%Y-%m")

# now that i have told python about the format, i will seperate the year and month 
monthly_data["Year"] = monthly_data["year"].dt.year
monthly_data["Month"] = monthly_data["year"].dt.month 


df_cleaned = monthly_data.pivot( index=["code", "name", "Year"], columns="Month", values="Average Surface Air Temperature",)


df_cleaned = df_cleaned.reindex(columns=range(1, 13))

df_cleaned.columns = [ "Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul","Aug", "Sep","Oct","Nov", "Dec",]

df_cleaned = df_cleaned.reset_index()


# add a column with the country name, so that when i merge it is easy
df_cleaned.insert(0, "country", "Brazil")

# now what I get after cleaning this, I want to save in a new folder 
df_cleaned.to_excel("data/clean/temp/Brazil_temp.xlsx", index=False,) 


