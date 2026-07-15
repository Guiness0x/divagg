import csv
import sys

REGISTRY_FILE = "../data/registry/tickers.csv"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: TICKER LOOKUP")
print(divider)

ticker_search = input(
    "\nTicker lookup : "
).strip().upper()

match = None

try:

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            if row["ticker"].upper() == ticker_search:
                match = row
                break

except FileNotFoundError:

    print("\n[ERROR] Registry file not found.")
    sys.exit(1)

except Exception as error:

    print(f"\n[ERROR] {error}")
    sys.exit(1)

if not match:

    print("\n[INFO] Ticker not found in registry.")
    sys.exit(0)

print("\nREGISTRY MATCH:\n")

print(subdivider)

print(f"TICKER           : {match['ticker']}")
print(f"NAME             : {match['name']}")
print(f"SECTOR           : {match['sector']}")
print(f"ASSET TYPE       : {match['asset_type']}")
print(f"PAYOUT FREQUENCY : {match['payout_frequency']}")

print(subdivider)

print(divider)
print("END LOOKUP")
print(divider)
