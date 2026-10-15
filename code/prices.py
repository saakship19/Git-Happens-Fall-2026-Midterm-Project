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

def build_price_files():	
	"""Create combined monthly prices and yearly average prices."""
	arabica = load_price_file(
		ARABICA_FILE,
		"PCOFFOTMUSDM",
		"arabica_cents_lb",
	)
	robusta = load_price_file(
		ROBUSTA_FILE,
		"PCOFFROBUSDM",
		"robusta_cents_lb",
	)

	monthly = arabica.merge(
		robusta,
		on="date",
		how="inner",
		validate="one_to_one",
	)

	monthly["year"] = monthly["date"].dt.year
	monthly["month"] = monthly["date"].dt.month

	monthly = monthly[
		[
			"year",
			"month",
			"date",
			"arabica_cents_lb",
			"robusta_cents_lb",
		]
	].sort_values("date")

	CLEAN_DIR.mkdir(parents=True, exist_ok=True)
	monthly.to_csv(MONTHLY_FILE, index=False)

	yearly = monthly.groupby("year", as_index=False).agg(
		arabica_cents_lb=("arabica_cents_lb", "mean"),
		robusta_cents_lb=("robusta_cents_lb", "mean"),
		months=("month", "nunique"),
	)

	yearly = monthly.groupby("year", as_index=False).agg(
		arabica_cents_lb=("arabica_cents_lb", "mean"),
		robusta_cents_lb=("robusta_cents_lb", "mean"),
		months=("month", "nunique"),
	)

	yearly = yearly[yearly["months"] == 12].drop(columns="months")
	yearly["arabica_pct_change"] = (
		yearly["arabica_cents_lb"].pct_change() * 100
	)

	yearly[
		["year","arabica_cents_lb", "arabica_pct_change"]
	].to_csv(ARABICA_CLEAN_FILE, index=False)

	yearly[
		["year", "robusta_cents_lb"]
	].to_csv(ROBUSTA_CLEAN_FILE, index=False)
	yearly["arabica_pct_change"] = (
		yearly["arabica_cents_lb"].pct_change() * 100
	)

	yearly[
		["year", "arabica_cents_lb", "arabica_pct_change"]
	].to_csv(ARABICA_CLEAN_FILE, index=False)

	yearly.to_csv(YEARLY_FILE, index=False)

if __name__ == "__main__":
	build_price_files()


