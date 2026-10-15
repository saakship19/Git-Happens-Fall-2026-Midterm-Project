import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data/clean/coffee_combined.csv")
df = df[df["Year"].between(2000, 2024)]

robusta_df = df[
    ~df["Country"].isin(["Colombia", "Ethiopia"])
]


# Average country weather by year.
# Global prices repeat across countries, averages unchanged

arabica_yearly = df.groupby("Year")[
    [
        "Annual_Average_Temperature",
        "Average_Precipitation",
        "arabica_cents_lb",
    ]
].mean()

robusta_yearly = robusta_df.groupby("Year")[
    [
        "Annual_Average_Temperature",
        "Average_Precipitation",
        "robusta_cents_lb",
    ]
].mean()


arabica_yearly = arabica_yearly.rename(
    columns={
        "Annual_Average_Temperature": "Temperature",
        "Average_Precipitation": "Precipitation",
        "arabica_cents_lb": "Arabica price",
    }
)

robusta_yearly = robusta_yearly.rename(
    columns={
        "Annual_Average_Temperature": "Temperature",
        "Average_Precipitation": "Precipitation",
        "robusta_cents_lb": "Robusta price",
    }
)


# Standardize annual temp, annual precip, annual price (across time) using its own 2000–2024 mean and standard deviation

arabica_standardized = (
    arabica_yearly - arabica_yearly.mean()
) / arabica_yearly.std()

robusta_standardized = (
    robusta_yearly - robusta_yearly.mean()
) / robusta_yearly.std()
