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
print("DIVAGG :: DIVERSIFICATION ANALYSIS")
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
# Analyze Diversification
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

            position_value = shares * dividend

            if ticker not in registry:
                continue

            sector = registry[ticker]["sector"]

            sector_totals[sector] += position_value
            portfolio_total += position_value

except Exception as error:

    print(
        f"\n[ERROR] Diversification analysis failed :: "
        f"{error}"
    )

    sys.exit(1)

if portfolio_total <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Output
#

print("\nSECTOR DIVERSIFICATION:\n")

table_header = (
    f"{'SECTOR':<30}"
    f"{'ALLOCATION':>15}"
)

print(table_header)
print(subdivider)

sorted_sectors = sorted(
    sector_totals.items(),
    key=lambda item: item[1],
    reverse=True
)

largest_sector = None
largest_percentage = 0.0

for sector, value in sorted_sectors:

    percentage = (
        value / portfolio_total
    ) * 100

    if percentage > largest_percentage:

        largest_sector = sector
        largest_percentage = percentage

    output_line = (
        f"{sector:<30}"
        f"{percentage:>14.2f}%"
    )

    print(output_line)

print(subdivider)

print(
    f"{'DOMINANT SECTOR':<30}"
    f"{largest_sector}"
)

print(
    f"{'DOMINANT EXPOSURE':<30}"
    f"{largest_percentage:.2f}%"
)

print(divider)
print("END DIVERSIFICATION")
print(divider)
