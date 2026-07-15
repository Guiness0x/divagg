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

STRESS_LEVELS = [
    0.10,
    0.20,
    0.30
]

print(divider)
print("DIVAGG :: YIELD STRESS")
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

#
# Baseline Income
#

baseline_annual = 0.0

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

    baseline_annual += annual_income

baseline_monthly = (
    baseline_annual / 12
)

print("\nYIELD STRESS ANALYSIS:\n")

print(subdivider)

print(
    f"{'STRESS LEVEL':<20}"
    f"{'ANNUAL FLOW':<20}"
    f"{'MONTHLY FLOW':<20}"
)

print(subdivider)

for stress in STRESS_LEVELS:

    stressed_annual = (
        baseline_annual *
        (
            1 - stress
        )
    )

    stressed_monthly = (
        stressed_annual / 12
    )

    stress_percent = int(
        stress * 100
    )

    print(
        f"{str(stress_percent) + '% CUT':<20}"
        f"${stressed_annual:<19.2f}"
        f"${stressed_monthly:<19.2f}"
    )

print(subdivider)

print(
    f"{'BASELINE ANNUAL':<30}"
    f"${baseline_annual:,.2f}"
)

print(
    f"{'BASELINE MONTHLY':<30}"
    f"${baseline_monthly:,.2f}"
)

#
# Runtime Resilience Assessment
#

if baseline_monthly >= 300:

    resilience = (
        "STRONG"
    )

elif baseline_monthly >= 150:

    resilience = (
        "MODERATE"
    )

else:

    resilience = (
        "WEAK"
    )

print(
    f"{'INCOME RESILIENCE':<30}"
    f"{resilience}"
)

print(divider)
print("END YIELD STRESS")
print(divider)
