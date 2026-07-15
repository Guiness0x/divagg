import csv
import sys

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

divider = "=" * 60
subdivider = "-" * 60

positions = []

total_monthly_income = 0.0

print(divider)
print("DIVAGG :: INCOME EFFICIENCY")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

#
# Analyze Portfolio
#

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row["ticker"]

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

            total_monthly_income += monthly_income

            positions.append({
                "ticker": ticker,
                "monthly_income": monthly_income
            })

except Exception as error:

    print(f"\n[ERROR] Efficiency analysis failed :: {error}")
    sys.exit(1)

if total_monthly_income <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Sort by Efficiency
#

positions.sort(
    key=lambda p: p["monthly_income"],
    reverse=True
)

#
# Output
#

print("\nPOSITION EFFICIENCY:\n")

table_header = (
    f"{'TICKER':<10}"
    f"{'MONTHLY':>15}"
    f"{'CONTRIBUTION':>20}"
)

print(table_header)
print(subdivider)

top_position = None
top_percentage = 0.0

for position in positions:

    percentage = (
        position["monthly_income"] /
        total_monthly_income
    ) * 100

    if percentage > top_percentage:

        top_position = position["ticker"]
        top_percentage = percentage

    output_line = (
        f"{position['ticker']:<10}"
        f"{position['monthly_income']:>15,.2f}"
        f"{percentage:>19.2f}%"
    )

    print(output_line)

print(subdivider)

print(
    f"{'TOP POSITION':<25}"
    f"{top_position}"
)

print(
    f"{'TOP CONTRIBUTION':<25}"
    f"{top_percentage:.2f}%"
)

print(divider)
print("END EFFICIENCY")
print(divider)
