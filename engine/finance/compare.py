import csv
import sys
from pathlib import Path

PORTFOLIO_DIR = Path("../data/portfolios")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: PORTFOLIO COMPARISON")
print(divider)

#
# Discover Portfolios
#

portfolio_files = sorted(
    PORTFOLIO_DIR.glob("*.csv")
)

if len(portfolio_files) < 2:

    print("\n[ERROR] At least two portfolios required.")
    sys.exit(1)

portfolios = [
    file.stem
    for file in portfolio_files
]

print("\nAVAILABLE PORTFOLIOS:\n")

for index, portfolio in enumerate(portfolios, start=1):

    print(f"{index}. {portfolio}")

#
# Select Portfolios
#

selection_one = input(
    "\nFirst portfolio number : "
).strip()

selection_two = input(
    "Second portfolio number : "
).strip()

try:

    first_index = int(selection_one) - 1
    second_index = int(selection_two) - 1

    first_portfolio = portfolios[first_index]
    second_portfolio = portfolios[second_index]

except Exception:

    print("\n[ERROR] Invalid selection.")
    sys.exit(1)

#
# Portfolio Metrics
#

def analyze_portfolio(portfolio_name):

    portfolio_file = (
        PORTFOLIO_DIR /
        f"{portfolio_name}.csv"
    )

    position_count = 0
    monthly_total = 0.0
    yearly_total = 0.0

    with open(portfolio_file, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

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

            position_count += 1

    return {
        "positions": position_count,
        "monthly": monthly_total,
        "yearly": yearly_total
    }

try:

    first_metrics = analyze_portfolio(
        first_portfolio
    )

    second_metrics = analyze_portfolio(
        second_portfolio
    )

except Exception as error:

    print(f"\n[ERROR] Comparison failed :: {error}")
    sys.exit(1)

#
# Output
#

print("\nCOMPARISON RESULTS:\n")

table_header = (
    f"{'METRIC':<20}"
    f"{first_portfolio:<20}"
    f"{second_portfolio:<20}"
)

print(table_header)
print(subdivider)

metrics = [
    (
        "Positions",
        first_metrics["positions"],
        second_metrics["positions"]
    ),
    (
        "Monthly Income",
        f"${first_metrics['monthly']:.2f}",
        f"${second_metrics['monthly']:.2f}"
    ),
    (
        "Yearly Income",
        f"${first_metrics['yearly']:.2f}",
        f"${second_metrics['yearly']:.2f}"
    )
]

for metric in metrics:

    output_line = (
        f"{metric[0]:<20}"
        f"{str(metric[1]):<20}"
        f"{str(metric[2]):<20}"
    )

    print(output_line)

print(subdivider)

print(divider)
print("END COMPARISON")
print(divider)
