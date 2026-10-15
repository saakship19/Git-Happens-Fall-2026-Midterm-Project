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

# Temperature and Arabica price

arabica_standardized[
    ["Temperature", "Arabica price"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region temperature and Arabica price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/temperature_arabica_price.png",
    bbox_inches="tight",
)
plt.close()


# Temperature and Robusta price

robusta_standardized[
    ["Temperature", "Robusta price"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region temperature and Robusta price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/temperature_robusta_price.png",
    bbox_inches="tight",
)
plt.close()

# Precipitation and Arabica price

arabica_standardized[
    ["Precipitation", "Arabica price"]
].plot(
    figsize=(10, 6),
    color=["teal", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region precipitation and Arabica price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/precipitation_arabica_price.png",
    bbox_inches="tight",
)
plt.close()


# Precipitation and Robusta price

robusta_standardized[
    ["Precipitation", "Robusta price"]
].plot(
    figsize=(10, 6),
    color=["teal", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region precipitation and Robusta price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/precipitation_robusta_price.png",
    bbox_inches="tight",
)
plt.close()

# Temperature, precipitation, and Arabica price

arabica_standardized[
    ["Temperature", "Precipitation", "Arabica price"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "teal", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region weather and Arabica price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/weather_arabica_price.png",
    bbox_inches="tight",
)
plt.close()


# Temperature, precipitation, and Robusta price

robusta_standardized[
    ["Temperature", "Precipitation", "Robusta price"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "teal", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region weather and Robusta price, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/weather_robusta_price.png",
    bbox_inches="tight",
)
plt.close()

# Correlations shown in the plots

results = []

for weather in ["Temperature", "Precipitation"]:
    arabica_complete = arabica_yearly[
        [weather, "Arabica price"]
    ].dropna()

    robusta_complete = robusta_yearly[
        [weather, "Robusta price"]
    ].dropna()

    results.append({
        "Coffee price": "Arabica",
        "Weather variable": weather,
        "Countries": "Brazil, Colombia, Ethiopia, Indonesia, Vietnam",
        "Years with complete data": len(arabica_complete),
        "Correlation": arabica_complete[weather].corr(
            arabica_complete["Arabica price"]
        ),
    })

    results.append({
        "Coffee price": "Robusta",
        "Weather variable": weather,
        "Countries": "Brazil, Indonesia, Vietnam",
        "Years with complete data": len(robusta_complete),
        "Correlation": robusta_complete[weather].corr(
            robusta_complete["Robusta price"]
        ),
    })

pd.DataFrame(results).to_csv(
    "artifacts/weather_price_correlations.csv",
    index=False,
)





# PRODUCTION GRAPHS

# Add yearly production totals to current yearly data
arabica_production = arabica_yearly.copy()
arabica_production["Arabica production"] = df.groupby("Year")[
    "Arabica_Production"
].sum()

robusta_production = robusta_yearly.copy()
robusta_production["Robusta production"] = robusta_df.groupby("Year")[
    "Robusta_Production"
].sum()

# Standardize weather, production, and prices scale
arabica_production_standardized = (
    arabica_production - arabica_production.mean()
) / arabica_production.std()

robusta_production_standardized = (
    robusta_production - robusta_production.mean()
) / robusta_production.std()



# Temperature and Arabica production

arabica_production_standardized[
    ["Temperature", "Arabica production"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region temperature and Arabica production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/temperature_arabica_production.png",
    bbox_inches="tight",
)
plt.close()


# Temperature and Robusta production

robusta_production_standardized[
    ["Temperature", "Robusta production"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region temperature and Robusta production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/temperature_robusta_production.png",
    bbox_inches="tight",
)
plt.close()


# Precipitation and Arabica production

arabica_production_standardized[
    ["Precipitation", "Arabica production"]
].plot(
    figsize=(10, 6),
    color=["teal", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region precipitation and Arabica production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/precipitation_arabica_production.png",
    bbox_inches="tight",
)
plt.close()


# Precipitation and Robusta production

robusta_production_standardized[
    ["Precipitation", "Robusta production"]
].plot(
    figsize=(10, 6),
    color=["teal", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region precipitation and Robusta production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/precipitation_robusta_production.png",
    bbox_inches="tight",
)
plt.close()



# Temperature, precipitation, and Arabica production
arabica_production_standardized[
    ["Temperature", "Precipitation", "Arabica production"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "teal", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region weather and Arabica production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/weather_arabica_production.png",
    bbox_inches="tight",
)
plt.close()


# Temperature, precipitation, and Robusta production
robusta_production_standardized[
    ["Temperature", "Precipitation", "Robusta production"]
].plot(
    figsize=(10, 6),
    color=["darkorange", "teal", "forestgreen"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Growing-region weather and Robusta production, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/weather_robusta_production.png",
    bbox_inches="tight",
)
plt.close()


# Arabica production and Arabica prices
arabica_production_standardized[
    ["Arabica production", "Arabica price"]
].plot(
    figsize=(10, 6),
    color=["forestgreen", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Arabica production and prices, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/arabica_production_price.png",
    bbox_inches="tight",
)
plt.close()


# Robusta production and Robusta prices
robusta_production_standardized[
    ["Robusta production", "Robusta price"]
].plot(
    figsize=(10, 6),
    color=["forestgreen", "navy"],
    xlabel="Year",
    ylabel="Standard deviations from 2000–2024 mean",
    title="Robusta production and prices, 2000–2024",
)

plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.savefig(
    "artifacts/robusta_production_price.png",
    bbox_inches="tight",
)
plt.close()



# Correlations between weather, prices, and coffee production

production_results = []

for coffee_type, yearly, production, price, countries in [
    (
        "Arabica",
        arabica_production,
        "Arabica production",
        "Arabica price",
        "Brazil, Colombia, Ethiopia, Indonesia, Vietnam",
    ),
    (
        "Robusta",
        robusta_production,
        "Robusta production",
        "Robusta price",
        "Brazil, Indonesia, Vietnam",
    ),
]:
    for variable1, variable2 in [
        ("Temperature", production),
        ("Precipitation", production),
        (production, price),
    ]:
        complete = yearly[[variable1, variable2]].dropna()

        production_results.append({
            "Coffee type": coffee_type,
            "Variable 1": variable1,
            "Variable 2": variable2,
            "Countries": countries,
            "Years with complete data": len(complete),
            "Correlation": complete[variable1].corr(
                complete[variable2]
            ),
        })

pd.DataFrame(production_results).to_csv(
    "artifacts/production_correlations.csv",
    index=False,
)

