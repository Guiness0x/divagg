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
print("DIVAGG :: RISK ANALYSIS")
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

    print(f"\n[ERROR] Risk analysis failed :: {error}")
    sys.exit(1)

if total_monthly_income <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Output
#

print("\nPOSITION CONCENTRATION:\n")

table_header = (
    f"{'TICKER':<10}"
    f"{'CONTRIBUTION':>15}"
    f"{'RISK LEVEL':>20}"
)

print(table_header)
print(subdivider)

positions.sort(
    key=lambda p: p["monthly_income"],
    reverse=True
)

for position in positions:

    percentage = (
        position["monthly_income"] /
        total_monthly_income
    ) * 100

    if percentage >= 35:

        risk_level = "HIGH"

    elif percentage >= 20:

        risk_level = "MODERATE"

    else:

        risk_level = "LOW"

    output_line = (
        f"{position['ticker']:<10}"
        f"{percentage:>14.2f}%"
        f"{risk_level:>20}"
    )

    print(output_line)

print(subdivider)

print(divider)
print("END RISK ANALYSIS")
print(divider)
