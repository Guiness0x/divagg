import csv
from pathlib import Path
import sys

REGISTRY_FILE = Path("../data/registry/tickers.csv")

divider = "=" * 60

print(divider)
print("DIVAGG :: REGISTRY ADD")
print(divider)

#
# Load Existing Registry
#

existing_tickers = set()

try:

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            existing_tickers.add(
                row["ticker"].strip().upper()
            )

except Exception as error:

    print(f"\n[ERROR] Failed loading registry :: {error}")
    sys.exit(1)

#
# User Input
#

print("\nENTER REGISTRY DATA\n")

ticker = input(
    "Ticker            : "
).strip().upper()

if ticker in existing_tickers:

    print("\n[ERROR] Ticker already exists.")
    sys.exit(1)

name = input(
    "Name              : "
).strip()

sector = input(
    "Sector            : "
).strip()

asset_type = input(
    "Asset Type        : "
).strip().lower()

payout_frequency = input(
    "Payout Frequency  : "
).strip().lower()

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

if payout_frequency not in VALID_FREQUENCIES:

    print("\n[ERROR] Invalid payout frequency.")
    sys.exit(1)

#
# Append Registry Entry
#

try:

    with open(REGISTRY_FILE, "a", newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            ticker,
            name,
            sector,
            asset_type,
            payout_frequency
        ])

    print("\n[SUCCESS] Registry entry added.")

    print(
        f"{ticker} | "
        f"{name}"
    )

except Exception as error:

    print(f"\n[ERROR] Registry append failed :: {error}")
    sys.exit(1)

print(f"\n{divider}")
print("END REGISTRY ADD")
print(divider)
