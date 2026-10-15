# combining all 5 datasets into a single temperature data set 

import pandas as pd 


brazil = pd.read_excel("data/clean/per/Brazil_per.xlsx")
vietnam = pd.read_excel("data/clean/per/Vietnam_per.xlsx")
colombia = pd.read_excel("data/clean/per/Colombia_per.xlsx")
indonesia = pd.read_excel("data/clean/per/Indonesia_per.xlsx")
ethiopia = pd.read_excel("data/clean/per/Ethiopia_per.xlsx")

# combining all these datasets

combined= pd.concat([brazil, vietnam, colombia, indonesia, ethiopia], ignore_index=True,)


# dropping a column with the country and district code 
combined = combined.drop(columns=["code"])

combined = combined.sort_values(["country", "name", "Year"])

#adding a column which will calcuate the average temperature for that year and province 
combined["Average_Precipitation"] = combined.loc[:, "Jan":"Dec"].mean(axis=1)

# saving them 



combined.to_csv("data/clean/precipitation_combined.csv", index=False, encoding="utf-8-sig") 
