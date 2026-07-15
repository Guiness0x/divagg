import csv
import sys
from collections import defaultdict

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: PAYOUT ANALYSIS")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

#
# Analyze Payout Structure
#

frequency_totals = defaultdict(float)

portfolio_total = 0.0

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

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

            frequency_totals[
                frequency
            ] += monthly_income

            portfolio_total += monthly_income

except Exception as error:

    print(
        f"\n[ERROR] Payout analysis failed :: "
        f"{error}"
    )

    sys.exit(1)

if portfolio_total <= 0:

    print("\n[ERROR] Portfolio total is zero.")
    sys.exit(1)

#
# Output
#

print("\nPAYOUT DISTRIBUTION:\n")

table_header = (
    f"{'FREQUENCY':<20}"
    f"{'ALLOCATION':>15}"
)

print(table_header)
print(subdivider)

sorted_frequencies = sorted(
    frequency_totals.items(),
    key=lambda item: item[1],
    reverse=True
)

dominant_frequency = None
dominant_percentage = 0.0

for frequency, value in sorted_frequencies:

    percentage = (
        value / portfolio_total
    ) * 100

    if percentage > dominant_percentage:

        dominant_frequency = frequency
        dominant_percentage = percentage

    output_line = (
        f"{frequency:<20}"
        f"{percentage:>14.2f}%"
    )

    print(output_line)

print(subdivider)

print(
    f"{'DOMINANT PAYOUT':<25}"
    f"{dominant_frequency}"
)

print(
    f"{'DOMINANT EXPOSURE':<25}"
    f"{dominant_percentage:.2f}%"
)

print(divider)
print("END PAYOUT ANALYSIS")
print(divider)
