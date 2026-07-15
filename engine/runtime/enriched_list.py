import csv
import sys

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

REGISTRY_FILE = "../data/registry/tickers.csv"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: ENRICHED PORTFOLIO LIST")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

#
# Load Registry
#

registry = {}

try:

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            registry[
                row["ticker"].upper()
            ] = row

except Exception as error:

    print(f"\n[ERROR] Registry load failed :: {error}")
    sys.exit(1)

#
# Load Portfolio
#

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        table_header = (
            f"{'TICKER':<10}"
            f"{'SECTOR':<25}"
            f"{'ASSET TYPE':<20}"
            f"{'PAYOUT':<15}"
        )

        print("\n")
        print(table_header)
        print(subdivider)

        row_count = 0

        for row in reader:

            ticker = row["ticker"].upper()

            if ticker not in registry:

                sector = "UNKNOWN"
                asset_type = "UNKNOWN"
                payout = "UNKNOWN"

            else:

                metadata = registry[ticker]

                sector = metadata["sector"]
                asset_type = metadata["asset_type"]
                payout = metadata["payout_frequency"]

            output_line = (
                f"{ticker:<10}"
                f"{sector:<25}"
                f"{asset_type:<20}"
                f"{payout:<15}"
            )

            print(output_line)

            row_count += 1

        print(subdivider)

        print(f"TOTAL POSITIONS : {row_count}")

except Exception as error:

    print(f"\n[ERROR] Portfolio load failed :: {error}")
    sys.exit(1)

print(divider)
print("END ENRICHED LIST")
print(divider)
