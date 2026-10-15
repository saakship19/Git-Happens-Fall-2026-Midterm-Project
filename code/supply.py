import pandas as pd 

df = pd.read_csv("data/raw/psd_coffee.csv")
print(df.head())
print(df.columns.tolist())
print("Total rows:", len(df))
print(df["Attribute_Description"].unique())