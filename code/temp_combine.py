# combining all 5 datasets into a single temperature data set 

import pandas as pd 


brazil = pd.read_excel("data/clean/temp/Brazil_temp.xlsx")
vietnam = pd.read_excel("data/clean/temp/Vietnam_temp.xlsx")
colombia = pd.read_excel("data/clean/temp/Colombia_temp.xlsx")
indonesia = pd.read_excel("data/clean/temp/Indonesia_temp.xlsx")
ethiopia = pd.read_excel("data/clean/temp/Ethiopia_temp.xlsx")

# combining all these datasets

combined= pd.concat([brazil, vietnam, colombia, indonesia, ethiopia], ignore_index=True,)


# dropping a column with the country and district code 
combined = combined.drop(columns=["code"])

combined = combined.sort_values(["country", "name", "Year"])

#adding a column which will calcuate the average temperature for that year and province 
combined["Annual_Average_Temperature"] = combined.loc[:, "Jan":"Dec"].mean(axis=1)

# saving them 

#combined.to_excel("data/clean/tas_combined.xlsx", index=False)

combined.to_csv("data/clean/temperature_combined.csv", index=False, encoding="utf-8-sig") 
