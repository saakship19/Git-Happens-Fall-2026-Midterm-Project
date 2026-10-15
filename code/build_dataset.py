import os

import pandas as pd

CLEAN_DIR = os.path.join("data", "clean")
ARABICA_PRICE_PATH = os.path.join(CLEAN_DIR, "price_arabica_clean.csv")
ROBUSTA_PRICE_PATH = os.path.join(CLEAN_DIR, "price_robusta_clean.csv")
ARABICA_PRODUCTION_PATH = os.path.join(CLEAN_DIR, "production_arabica_clean.csv")
ROBUSTA_PRODUCTION_PATH = os.path.join(CLEAN_DIR, "production_robusta_clean.csv")
RAIN_PATH = os.path.join(CLEAN_DIR, "precipitation_combined.csv")
TEMP_PATH = os.path.join(CLEAN_DIR, "temperature_combined.csv")

START_YEAR = 2000
END_YEAR = 2024

COUNTRY_PATH = os.path.join(CLEAN_DIR, "coffee_by_country.csv")
YEAR_PATH = os.path.join(CLEAN_DIR, "coffee_by_year.csv")

def load_prices():

    """Combine the two price (Arabica and Robusta) files into one table.
    Input: none.
    Output: a table of yearly Arabica and Robusta prices.
    """
    
    arabica = pd.read_csv(ARABICA_PRICE_PATH, encoding="utf-8-sig")
    robusta = pd.read_csv(ROBUSTA_PRICE_PATH, encoding="utf-8-sig")

    prices = arabica.merge(robusta, on="year")
    prices = prices.rename(columns={"year": "Year"})
    prices = prices.sort_values("Year")
    
    return prices


def load_weather():
    """Average each country's regions and add anomalies.
	Input: none.
    Output: one row per country per year with rain, temperature, and anomalies.
    """
    rain = pd.read_csv(RAIN_PATH, encoding="utf-8-sig")
    temp = pd.read_csv(TEMP_PATH, encoding="utf-8-sig")

    rain = rain.rename(columns={"country": "Country"})
    temp = temp.rename(columns={"country": "Country"})

    rain = rain.groupby(["Country", "Year"], as_index=False)[
        "Average_Precipitation"
    ].mean()
    temp = temp.groupby(["Country", "Year"], as_index=False)[
        "Annual_Average_Temperature"
    ].mean()

    weather = rain.merge(temp, on=["Country", "Year"])

    after_start = weather["Year"] >= START_YEAR
    before_end = weather["Year"] <= END_YEAR
    weather = weather[after_start & before_end].copy()

    rain_by_country = weather.groupby("Country")["Average_Precipitation"]
    temp_by_country = weather.groupby("Country")["Annual_Average_Temperature"]
    normal_rain = rain_by_country.transform("mean")
    normal_temp = temp_by_country.transform("mean")

    weather["Precipitation_Anomaly"] = weather["Average_Precipitation"] - normal_rain
    weather["Temperature_Anomaly"] = weather["Annual_Average_Temperature"] - normal_temp
    return weather

