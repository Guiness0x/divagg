import csv
import sys

INPUT_FILE = "../data/portfolio.csv"

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

divider = "=" * 60
subdivider = "-" * 60

positions = []

total_monthly_income = 0.0

print(divider)
print("DIVAGG :: PORTFOLIO ANALYTICS")
print(divider)

try:

    with open(INPUT_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row['ticker']
            shares = float(row['shares'])
            dividend = float(row['dividend'])
            frequency = row['frequency'].lower()

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

except FileNotFoundError:

    print("[ERROR] portfolio.csv not found.")
    sys.exit(1)

except Exception as error:

    print(f"[ERROR] {error}")
    sys.exit(1)

if total_monthly_income <= 0:

    print("[ERROR] Total monthly income is zero.")
    sys.exit(1)

positions.sort(
    key=lambda p: p["monthly_income"],
    reverse=True
)

print("\nINCOME CONTRIBUTION:\n")

table_header = (
    f"{'TICKER':<10}"
    f"{'MONTHLY':>15}"
    f"{'PORTFOLIO %':>20}"
)

print(table_header)
print(subdivider)

for position in positions:

    percentage = (
        position["monthly_income"] /
        total_monthly_income
    ) * 100

    output_line = (
        f"{position['ticker']:<10}"
        f"{position['monthly_income']:>15,.2f}"
        f"{percentage:>19.2f}%"
    )

    print(output_line)

print(subdivider)

print(
    f"{'TOTAL':<10}"
    f"{total_monthly_income:>15,.2f}"
    f"{100:>19.2f}%"
)

print(divider)
print("END ANALYTICS")
print(divider)
