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

#
# Recovery Simulation Settings
#

STRESS_CUT = 0.30
RECOVERY_GROWTH = 0.08

print(divider)
print("DIVAGG :: RECOVERY SIM")
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

#
# Stress State
#

stressed_annual = (
    baseline_annual *
    (
        1 - STRESS_CUT
    )
)

#
# Recovery Simulation
#

current_income = stressed_annual

years = 0

while current_income < baseline_annual:

    current_income *= (
        1 + RECOVERY_GROWTH
    )

    years += 1

recovered_monthly = (
    current_income / 12
)

print("\nRECOVERY ANALYSIS:\n")

print(subdivider)

print(
    f"{'BASELINE ANNUAL':<30}"
    f"${baseline_annual:,.2f}"
)

print(
    f"{'BASELINE MONTHLY':<30}"
    f"${baseline_monthly:,.2f}"
)

print(subdivider)

print(
    f"{'STRESS CUT':<30}"
    f"{int(STRESS_CUT * 100)}%"
)

print(
    f"{'STRESSED ANNUAL':<30}"
    f"${stressed_annual:,.2f}"
)

print(subdivider)

print(
    f"{'RECOVERY GROWTH':<30}"
    f"{int(RECOVERY_GROWTH * 100)}%"
)

print(
    f"{'RECOVERY YEARS':<30}"
    f"{years}"
)

print(
    f"{'RECOVERED MONTHLY':<30}"
    f"${recovered_monthly:,.2f}"
)

print(subdivider)

#
# Runtime Recovery Assessment
#

if years <= 3:

    recovery_status = (
        "FAST RECOVERY"
    )

elif years <= 6:

    recovery_status = (
        "MODERATE RECOVERY"
    )

else:

    recovery_status = (
        "SLOW RECOVERY"
    )

print(
    f"{'RECOVERY STATUS':<30}"
    f"{recovery_status}"
)

print(divider)
print("END RECOVERY SIM")
print(divider)
