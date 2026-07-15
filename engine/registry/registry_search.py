import csv
import sys
from pathlib import Path

REGISTRY_FILE = (
    Path("../data/registry/tickers.csv")
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: REGISTRY SEARCH")
print(divider)

search_term = input(
    "\nSearch registry : "
).strip().lower()

matches = []

try:

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            searchable_fields = [
                row["ticker"],
                row["name"],
                row["sector"],
                row["asset_type"],
                row["payout_frequency"]
            ]

            searchable_text = " ".join(
                searchable_fields
            ).lower()

            if search_term in searchable_text:

                matches.append(row)

except FileNotFoundError:

    print("\n[ERROR] Registry file not found.")
    sys.exit(1)

except Exception as error:

    print(f"\n[ERROR] {error}")
    sys.exit(1)

if not matches:

    print("\n[INFO] No registry matches found.")
    sys.exit(0)

print("\nREGISTRY MATCHES:\n")

table_header = (
    f"{'TICKER':<10}"
    f"{'ASSET TYPE':<20}"
    f"{'PAYOUT':<15}"
    f"{'SECTOR':<25}"
)

print(table_header)
print(subdivider)

for row in matches:

    output_line = (
        f"{row['ticker']:<10}"
        f"{row['asset_type']:<20}"
        f"{row['payout_frequency']:<15}"
        f"{row['sector']:<25}"
    )

    print(output_line)

print(subdivider)

print(f"TOTAL MATCHES : {len(matches)}")

print(divider)
print("END REGISTRY SEARCH")
print(divider)
