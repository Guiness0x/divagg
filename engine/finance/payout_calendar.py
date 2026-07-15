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

MONTHS = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC"
]

print(divider)
print("DIVAGG :: PAYOUT CALENDAR")
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

monthly_income_map = {
    month: 0.0
    for month in MONTHS
}

#
# Simplified Cadence Model
#

quarterly_months = [
    "MAR",
    "JUN",
    "SEP",
    "DEC"
]

for row in rows:

    dividend_yield = float(
        row.get(
            "dividend_yield",
            0.0
        )
    )

    payout_frequency = (
        row.get(
            "payout_frequency"
        )
        or ""
    ).lower()

    annual_income = (
        ALLOCATION_PER_ASSET *
        (
            dividend_yield / 100
        )
    )

    if payout_frequency == "monthly":

        monthly_amount = (
            annual_income / 12
        )

        for month in MONTHS:

            monthly_income_map[
                month
            ] += monthly_amount

    elif payout_frequency == "quarterly":

        quarterly_amount = (
            annual_income / 4
        )

        for month in quarterly_months:

            monthly_income_map[
                month
            ] += quarterly_amount

print("\nPROJECTED PAYOUT RHYTHM:\n")

print(subdivider)

print(
    f"{'MONTH':<10}"
    f"{'PROJECTED INCOME':<20}"
)

print(subdivider)

annual_total = 0.0

for month in MONTHS:

    amount = (
        monthly_income_map[
            month
        ]
    )

    annual_total += amount

    print(
        f"{month:<10}"
        f"${amount:<19.2f}"
    )

print(subdivider)

print(
    f"{'PROJECTED ANNUAL':<30}"
    f"${annual_total:,.2f}"
)

print(divider)
print("END PAYOUT CALENDAR")
print(divider)
