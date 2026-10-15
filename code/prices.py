from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")

ARABICA_FILE = RAW_DIR / "arabica.csv"
ROBUSTA_FILE = RAW_DIR / "robusta.csv"

MONTHLY_FILE = CLEAN_DIR / "prices_monthly.csv"
YEARLY_FILE = CLEAN_DIR / "prices.csv"
ARABICA_CLEAN_FILE = CLEAN_DIR / "price_arabica_clean.csv"
ROBUSTA_CLEAN_FILE = CLEAN_DIR / "price_robusta_clean.csv"

def load_price_file(file_path, source_column, output_column):
	"""Read a monthly price CSV and return its date and price column. """
	data = pd.read_csv(file_path)
	data["observation_date"] = pd.to_datetime(
		data["observation_date"]
	)
	data[source_column] = pd.to_numeric(
		data[source_column],
		errors="coerce",
	)
	data = data.dropna(subset=[source_column])

	data = data.rename(
		columns={
			"observation_date": "date",
			source_column: output_column,
		}
	)

	return data[["date", output_column]]