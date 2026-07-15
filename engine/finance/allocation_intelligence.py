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
print("DIVAGG :: ALLOCATION INTELLIGENCE")
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

        ticker = row.get("ticker")

        if not ticker:
            continue

        rows.append(row)

category_income = {
    "ETF / INCOME FUNDS": 0.0,
    "REITS": 0.0,
    "EQUITIES": 0.0
}

total_income = 0.0

for row in rows:

    asset_type = (
        row.get("asset_type")
        or ""
    ).lower()

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

    if asset_type in [
        "dividend_etf",
        "income_fund"
    ]:

        category_income[
            "ETF / INCOME FUNDS"
        ] += annual_income

    elif asset_type == "reit":

        category_income[
            "REITS"
        ] += annual_income

    elif asset_type == "equity":

        category_income[
            "EQUITIES"
        ] += annual_income

print("\nALLOCATION EXPOSURE:\n")

print(subdivider)

print(
    f"{'CATEGORY':<25}"
    f"{'ANNUAL FLOW':<20}"
    f"{'EXPOSURE':<15}"
    f"{'STATUS':<15}"
)

print(subdivider)

for category, income in category_income.items():

    if total_income == 0:

        exposure = 0.0

    else:

        exposure = (
            income /
            total_income
        ) * 100

    if exposure >= 60:

        status = "OVERWEIGHT"

    elif exposure >= 25:

        status = "BALANCED"

    elif exposure > 0:

        status = "UNDERWEIGHT"

    else:

        status = "EMPTY"

    print(
        f"{category:<25}"
        f"${income:<19.2f}"
        f"{exposure:<14.2f}%"
        f"{status:<15}"
    )

print(subdivider)

print(
    f"{'TOTAL ANNUAL FLOW':<30}"
    f"${total_income:,.2f}"
)

print(subdivider)

dominant_category = max(
    category_income,
    key=category_income.get
)

dominant_exposure = (
    category_income[
        dominant_category
    ] / total_income
) * 100

if dominant_exposure >= 60:

    allocation_status = "CONCENTRATED"

elif dominant_exposure >= 45:

    allocation_status = "MODERATE TILT"

else:

    allocation_status = "BALANCED"

print(
    f"{'DOMINANT CATEGORY':<30}"
    f"{dominant_category}"
)

print(
    f"{'DOMINANT EXPOSURE':<30}"
    f"{dominant_exposure:.2f}%"
)

print(
    f"{'ALLOCATION STATUS':<30}"
    f"{allocation_status}"
)

print(divider)
print("END ALLOCATION INTELLIGENCE")
print(divider)
