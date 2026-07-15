import csv
import sys
from collections import defaultdict

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

REGISTRY_FILE = "../data/registry/tickers.csv"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SECTOR ANALYSIS")
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
# Analyze Portfolio
#

sector_totals = defaultdict(float)

portfolio_total = 0.0

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row["ticker"].upper()

            shares = float(row["shares"])
            dividend = float(row["dividend"])

            value = shares * dividend

            if ticker not in registry:
                continue

            sector = registry[ticker]["sector"]

            sector_totals[sector] += value
            portfolio_total += value

except Exception as error:

    print(f"\n[ERROR] Portfolio analysis failed :: {error}")
    sys.exit(1)

if portfolio_total <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Output
#

print("\nSECTOR EXPOSURE:\n")

table_header = (
    f"{'SECTOR':<30}"
    f"{'EXPOSURE %':>15}"
)

print(table_header)
print(subdivider)

sorted_sectors = sorted(
    sector_totals.items(),
    key=lambda item: item[1],
    reverse=True
)

for sector, value in sorted_sectors:

    percentage = (
        value / portfolio_total
    ) * 100

    output_line = (
        f"{sector:<30}"
        f"{percentage:>14.2f}%"
    )

    print(output_line)

print(subdivider)

print(
    f"{'TOTAL':<30}"
    f"{100:>14.2f}%"
)

print(divider)
print("END SECTOR ANALYSIS")
print(divider)
