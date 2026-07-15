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
print("DIVAGG :: PORTFOLIO HEALTH")
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
# Analysis Containers
#

sector_totals = defaultdict(float)
frequency_totals = defaultdict(float)

positions = []

portfolio_total = 0.0

#
# Analyze Portfolio
#

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row["ticker"].upper()

            shares = float(row["shares"])
            dividend = float(row["dividend"])
            frequency = row["frequency"].lower()

            payout = shares * dividend

            if frequency == "monthly":

                monthly_income = payout

            elif frequency == "quarterly":

                monthly_income = (
                    payout * 4
                ) / 12

            elif frequency == "yearly":

                monthly_income = payout / 12

            else:
                continue

            portfolio_total += monthly_income

            positions.append({
                "ticker": ticker,
                "monthly_income": monthly_income
            })

            frequency_totals[
                frequency
            ] += monthly_income

            if ticker in registry:

                sector = registry[ticker]["sector"]

                sector_totals[
                    sector
                ] += monthly_income

except Exception as error:

    print(
        f"\n[ERROR] Health analysis failed :: "
        f"{error}"
    )

    sys.exit(1)

if portfolio_total <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Health Score
#

health_score = 100

#
# Sector Dominance
#

largest_sector = max(
    sector_totals.values()
)

largest_sector_percentage = (
    largest_sector /
    portfolio_total
) * 100

if largest_sector_percentage > 50:

    health_score -= 15

#
# Payout Dominance
#

largest_frequency = max(
    frequency_totals.values()
)

largest_frequency_percentage = (
    largest_frequency /
    portfolio_total
) * 100

if largest_frequency_percentage > 70:

    health_score -= 10

#
# Position Concentration
#

highest_position = max(
    positions,
    key=lambda p: p["monthly_income"]
)

highest_position_percentage = (
    highest_position["monthly_income"] /
    portfolio_total
) * 100

if highest_position_percentage > 35:

    health_score -= 20

#
# Classification
#

if health_score >= 85:

    status = "STRONG"

elif health_score >= 70:

    status = "STABLE"

elif health_score >= 50:

    status = "CAUTION"

else:

    status = "HIGH RISK"

#
# Output
#

print("\nHEALTH SUMMARY:\n")

print(subdivider)

print(
    f"{'HEALTH SCORE':<30}"
    f"{health_score}/100"
)

print(
    f"{'STATUS':<30}"
    f"{status}"
)

print(
    f"{'DOMINANT SECTOR':<30}"
    f"{largest_sector_percentage:.2f}%"
)

print(
    f"{'DOMINANT PAYOUT':<30}"
    f"{largest_frequency_percentage:.2f}%"
)

print(
    f"{'TOP POSITION':<30}"
    f"{highest_position_percentage:.2f}%"
)

print(subdivider)

print(divider)
print("END HEALTH")
print(divider)
