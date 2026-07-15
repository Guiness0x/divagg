import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LIVE_REGISTRY = (
    BASE_DIR /
    "data" /
    "live" /
    "live_registry.csv"
)

divider = "=" * 60
subdivider = "-" * 60

ALLOCATION_PER_ASSET = 10000

print(divider)
print("DIVAGG :: INCOME STABILITY")
print(divider)

if not LIVE_REGISTRY.exists():

    print("\n[ERROR] Live registry missing.")
    raise SystemExit(1)

rows = []

with open(
    LIVE_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        if not row:

            continue

        ticker = (
            row.get("ticker")
        )

        if not ticker:

            continue

        rows.append(row)

monthly_income = 0.0
quarterly_income = 0.0

reit_income = 0.0
etf_income = 0.0
equity_income = 0.0

total_income = 0.0

for row in rows:

    dividend_yield = float(
        row.get(
            "dividend_yield",
            0.0
        )
    )

    annual_income = (
        ALLOCATION_PER_ASSET *
        (
            dividend_yield / 100
        )
    )

    total_income += annual_income

    payout_frequency = (
        row.get(
            "payout_frequency"
        )
        or ""
    ).lower()

    asset_type = (
        row.get(
            "asset_type"
        )
        or ""
    ).lower()

    #
    # Cadence Aggregation
    #

    if payout_frequency == "monthly":

        monthly_income += annual_income

    elif payout_frequency == "quarterly":

        quarterly_income += annual_income

    #
    # Asset Aggregation
    #

    if asset_type == "reit":

        reit_income += annual_income

    elif asset_type in [
        "dividend_etf",
        "income_fund"
    ]:

        etf_income += annual_income

    elif asset_type == "equity":

        equity_income += annual_income

#
# Percentage Calculations
#

def calculate_percent(value):

    if total_income == 0:

        return 0.0

    return (
        value / total_income
    ) * 100

monthly_percent = calculate_percent(
    monthly_income
)

quarterly_percent = calculate_percent(
    quarterly_income
)

reit_percent = calculate_percent(
    reit_income
)

etf_percent = calculate_percent(
    etf_income
)

equity_percent = calculate_percent(
    equity_income
)

print("\nINCOME STABILITY ANALYSIS:\n")

print(subdivider)

print(
    f"{'CATEGORY':<30}"
    f"{'ANNUAL FLOW':<20}"
    f"{'EXPOSURE':<15}"
)

print(subdivider)

print(
    f"{'MONTHLY PAYOUTS':<30}"
    f"${monthly_income:<19.2f}"
    f"{monthly_percent:.2f}%"
)

print(
    f"{'QUARTERLY PAYOUTS':<30}"
    f"${quarterly_income:<19.2f}"
    f"{quarterly_percent:.2f}%"
)

print(subdivider)

print(
    f"{'ETF / INCOME FUNDS':<30}"
    f"${etf_income:<19.2f}"
    f"{etf_percent:.2f}%"
)

print(
    f"{'REITS':<30}"
    f"${reit_income:<19.2f}"
    f"{reit_percent:.2f}%"
)

print(
    f"{'EQUITIES':<30}"
    f"${equity_income:<19.2f}"
    f"{equity_percent:.2f}%"
)

print(subdivider)

#
# Runtime Assessment
#

if monthly_percent >= 50:

    cadence_status = (
        "STABLE MONTHLY FLOW"
    )

elif monthly_percent >= 30:

    cadence_status = (
        "BALANCED FLOW"
    )

else:

    cadence_status = (
        "QUARTERLY HEAVY"
    )

print(
    f"{'CADENCE STATUS':<30}"
    f"{cadence_status}"
)

print(divider)
print("END INCOME STABILITY")
print(divider)
