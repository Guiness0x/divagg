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

#
# Simulation Assumption
#
# Fixed example allocation
# per asset for Generation 0.2
#

ALLOCATION_PER_ASSET = 10000

print(divider)
print("DIVAGG :: INCOME PROJECTION")
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

print("\nPROJECTED INCOME FLOW:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'YIELD':<10}"
    f"{'ANNUAL':<15}"
    f"{'MONTHLY':<15}"
)

print(subdivider)

total_annual = 0.0

for row in rows:

    ticker = (
        row.get("ticker")
        or "UNKNOWN"
    )

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

    monthly_income = (
        annual_income / 12
    )

    total_annual += annual_income

    print(
        f"{ticker:<10}"
        f"{str(dividend_yield) + '%':<10}"
        f"${annual_income:<14.2f}"
        f"${monthly_income:<14.2f}"
    )

print(subdivider)

total_monthly = (
    total_annual / 12
)

portfolio_capital = (
    len(rows) *
    ALLOCATION_PER_ASSET
)

print(
    f"{'PORTFOLIO CAPITAL':<30}"
    f"${portfolio_capital:,.2f}"
)

print(
    f"{'PROJECTED ANNUAL':<30}"
    f"${total_annual:,.2f}"
)

print(
    f"{'PROJECTED MONTHLY':<30}"
    f"${total_monthly:,.2f}"
)

print(divider)
print("END INCOME PROJECTION")
print(divider)
