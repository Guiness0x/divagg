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

HIGH_RISK_THRESHOLD = 25.0
MODERATE_RISK_THRESHOLD = 15.0

print(divider)
print("DIVAGG :: CONCENTRATION RISK")
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

income_map = {}

total_income = 0.0

#
# Aggregate Income
#

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

    total_income += annual_income

    income_map[
        ticker
    ] = annual_income

#
# Risk Analysis
#

print("\nINCOME CONCENTRATION ANALYSIS:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'ANNUAL FLOW':<20}"
    f"{'EXPOSURE':<15}"
    f"{'RISK':<20}"
)

print(subdivider)

highest_exposure = 0.0
highest_ticker = "UNKNOWN"

for ticker, annual_income in income_map.items():

    exposure = (
        annual_income /
        total_income
    ) * 100

    if exposure > highest_exposure:

        highest_exposure = exposure
        highest_ticker = ticker

    if exposure >= HIGH_RISK_THRESHOLD:

        risk_status = (
            "HIGH"
        )

    elif exposure >= MODERATE_RISK_THRESHOLD:

        risk_status = (
            "MODERATE"
        )

    else:

        risk_status = (
            "LOW"
        )

    print(
        f"{ticker:<10}"
        f"${annual_income:<19.2f}"
        f"{exposure:<14.2f}%"
        f"{risk_status:<20}"
    )

print(subdivider)

#
# Runtime Assessment
#

if highest_exposure >= HIGH_RISK_THRESHOLD:

    portfolio_status = (
        "HIGH CONCENTRATION"
    )

elif highest_exposure >= MODERATE_RISK_THRESHOLD:

    portfolio_status = (
        "MODERATE CONCENTRATION"
    )

else:

    portfolio_status = (
        "BALANCED DISTRIBUTION"
    )

print(
    f"{'HIGHEST EXPOSURE':<30}"
    f"{highest_ticker}"
)

print(
    f"{'HIGHEST EXPOSURE %':<30}"
    f"{highest_exposure:.2f}%"
)

print(
    f"{'PORTFOLIO STATUS':<30}"
    f"{portfolio_status}"
)

print(divider)
print("END CONCENTRATION RISK")
print(divider)
