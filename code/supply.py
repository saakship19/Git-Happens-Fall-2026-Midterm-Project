import pandas as pd 

df = pd.read_csv("data/raw/psd_coffee.csv")
print(df.head())
print(df.columns.tolist())
print("Total rows:", len(df))
print(df["Attribute_Description"].unique())


#Arabica production
arabica = df[df["Attribute_Description"] == "Arabica Production"]

countries = ["Brazil", "Vietnam", "Colombia", "Indonesia", "Ethiopia"]
arabica = arabica[arabica["Country_Name"].isin(countries)]

arabica = arabica[
	(arabica["Market_Year"] >= 2000) &
	(arabica["Market_Year"] <= 2024)
]

print(arabica["Country_Name"].unique())
print("Arabica rows:", len(arabica))
print(arabica[["Country_Name", "Market_Year", "Value"]])


arabica = arabica[["Country_Name", "Market_Year", "Value"]]
print(arabica.head())
print("Total Arabica rows:", len(arabica))

arabica.columns = ["Country", "Year", "Arabica_Production"]
print(arabica.head())

print("Duplicate rows:", arabica.duplicated(subset=["Country", "Year"]).sum())
print("Missing values:")
print(arabica.isna().sum())

arabica.to_csv("data/clean/production_arabica_clean.csv", index=False)

#Robusta production
robusta = df[df["Attribute_Description"] == "Robusta Production"]

countries = ["Brazil", "Vietnam", "Colombia", "Indonesia", "Ethiopia"]
robusta = robusta[robusta["Country_Name"].isin(countries)]

robusta = robusta[
	(robusta["Market_Year"] >= 2000) &
	(robusta["Market_Year"] <= 2024)
]

print(robusta["Country_Name"].unique())
print("Robusta rows:", len(robusta))
print(robusta[["Country_Name", "Market_Year", "Value"]])

robusta = robusta[["Country_Name", "Market_Year", "Value"]]
print(robusta.head())
print("Total Robusta rows:", len(robusta))

robusta.columns = ["Country", "Year", "Robusta_Production"]
print(robusta.head())

print("Duplicate rows:", robusta.duplicated(subset=["Country", "Year"]).sum())
print("Missing values:")
print(robusta.isna().sum())

robusta.to_csv("data/clean/production_robusta_clean.csv", index=False)
