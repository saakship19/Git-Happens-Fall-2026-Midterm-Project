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

    return weather


def load_production():
    """Combine Arabica and Robusta production and add the total.
    Input: none.
    Output: one row per country per year with production.
    """
    arabica = pd.read_csv(ARABICA_PRODUCTION_PATH, encoding="utf-8-sig")
    robusta = pd.read_csv(ROBUSTA_PRODUCTION_PATH, encoding="utf-8-sig")

    production = arabica.merge(robusta, on=["Country", "Year"])
    production["Total_Production"] = (
        production["Arabica_Production"] + production["Robusta_Production"]
    )

    after_start = production["Year"] >= START_YEAR
    before_end = production["Year"] <= END_YEAR
    return production[after_start & before_end]


def make_country_table(production, weather):
    """Join production and weather.
	Input: the production and weather tables.
    Output: one row per country per year.
    """
    by_country = production.merge(weather, on=["Country", "Year"], how="inner")
    by_country = by_country.sort_values(["Country", "Year"])
    return by_country



def make_year_table(production, prices):
    """Add up the 5 countries each year and join prices.
    Input: the production and prices tables.
    Output: one row per year with production and prices.
    """
    amounts = ["Arabica_Production", "Robusta_Production", "Total_Production"]
    by_year = production.groupby("Year", as_index = False)[amounts].sum()

    by_year = by_year.merge(prices, on="Year", how="inner")
    by_year = by_year.sort_values("Year")
    return by_year


def build_dataset():
    """Build and save the 2 merged tables.

    Input: none.
    Output: none. Saves coffee_by_country.csv and coffee_by_year.csv.
    """
    prices = load_prices()
    weather = load_weather()
    production = load_production()

    by_country = make_country_table(production, weather)
    by_year = make_year_table(production, prices)

    by_country.to_csv(COUNTRY_PATH, index=False)
    by_year.to_csv(YEAR_PATH, index=False)


if __name__ == "__main__":
    build_dataset()
