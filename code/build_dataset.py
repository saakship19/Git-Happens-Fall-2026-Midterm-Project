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