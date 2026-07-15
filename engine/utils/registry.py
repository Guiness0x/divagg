import csv
from pathlib import Path

REGISTRY_FILE = (
    Path(__file__).resolve().parent.parent.parent.parent /
    "data" /
    "registry" /
    "tickers.csv"
)

def load_registry_tickers():

    tickers = set()

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row["ticker"].strip().upper()

            tickers.add(ticker)

    return tickers
