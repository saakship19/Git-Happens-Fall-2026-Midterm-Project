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