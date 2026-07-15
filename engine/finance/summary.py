import csv
import sys
from pathlib import Path
from collections import defaultdict

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

REGISTRY_FILE = Path("../data/registry/tickers.csv")
SNAPSHOT_DIR = Path("../snapshots")
AUDIT_LOG = Path("../logs/audit.log")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: OPERATIONAL SUMMARY")
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
# Containers
#

sector_totals = defaultdict(float)
frequency_totals = defaultdict(float)

positions = []

monthly_total = 0.0
yearly_total = 0.0

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
                yearly_income = payout * 12

            elif frequency == "quarterly":

                monthly_income = (
                    payout * 4
                ) / 12

                yearly_income = payout * 4

            elif frequency == "yearly":

                monthly_income = payout / 12
                yearly_income = payout

            else:
                continue

            monthly_total += monthly_income
            yearly_total += yearly_income

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
        f"\n[ERROR] Summary analysis failed :: "
        f"{error}"
    )

    sys.exit(1)

if monthly_total <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Dominant Sector
#

largest_sector_name = max(
    sector_totals,
    key=sector_totals.get
)

largest_sector_percentage = (
    sector_totals[largest_sector_name]
    / monthly_total
) * 100

#
# Dominant Payout
#

largest_frequency_name = max(
    frequency_totals,
    key=frequency_totals.get
)

largest_frequency_percentage = (
    frequency_totals[largest_frequency_name]
    / monthly_total
) * 100

#
# Top Position
#

top_position = max(
    positions,
    key=lambda p: p["monthly_income"]
)

top_position_percentage = (
    top_position["monthly_income"]
    / monthly_total
) * 100

#
# Health Score
#

health_score = 100

if largest_sector_percentage > 50:

    health_score -= 15

if largest_frequency_percentage > 70:

    health_score -= 10

if top_position_percentage > 35:

    health_score -= 20

#
# Health Classification
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
# Snapshot Count
#

snapshot_count = len(
    list(
        SNAPSHOT_DIR.glob(
            f"{ACTIVE_PORTFOLIO}_snapshot_*.csv"
        )
    )
)

#
# Audit Event Count
#

audit_count = 0

if AUDIT_LOG.exists():

    with open(AUDIT_LOG, "r") as logfile:

        audit_count = len(
            logfile.readlines()
        )

#
# Output
#

print("\nSYSTEM SUMMARY:\n")

print(subdivider)

print(
    f"{'MONTHLY INCOME':<30}"
    f"${monthly_total:.2f}"
)

print(
    f"{'YEARLY INCOME':<30}"
    f"${yearly_total:.2f}"
)

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
    f"{largest_sector_name}"
)

print(
    f"{'DOMINANT PAYOUT':<30}"
    f"{largest_frequency_name}"
)

print(
    f"{'TOP POSITION':<30}"
    f"{top_position['ticker']}"
)

print(
    f"{'PORTFOLIO SNAPSHOTS':<30}"
    f"{snapshot_count}"
)

print(
    f"{'AUDIT EVENTS':<30}"
    f"{audit_count}"
)

print(subdivider)

print(divider)
print("END SUMMARY")
print(divider)
