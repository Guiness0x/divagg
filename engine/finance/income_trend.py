import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

HISTORY_DIR = (
    BASE_DIR /
    "history_runtime"
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: INCOME TREND")
print(divider)

if not HISTORY_DIR.exists():

    print("\n[ERROR] Historical runtime directory missing.")
    raise SystemExit(1)

history_files = sorted(
    HISTORY_DIR.glob(
        "*.csv"
    )
)

if len(history_files) < 2:

    print("\n[ERROR] At least two historical snapshots required.")
    raise SystemExit(1)

print("\nHISTORICAL TREND ANALYSIS:\n")

print(subdivider)

print(
    f"{'SNAPSHOT':<40}"
    f"{'TOTAL ANNUAL FLOW':<20}"
)

print(subdivider)

totals = []

for snapshot in history_files:

    total_annual = 0.0

    with open(
        snapshot,
        newline="",
        encoding="utf-8"
    ) as csvfile:

        reader = csv.DictReader(
            csvfile
        )

        for row in reader:

            projected_income = float(
                row.get(
                    "projected_annual_income",
                    0.0
                )
            )

            total_annual += projected_income

    totals.append(total_annual)

    print(
        f"{snapshot.name:<40}"
        f"${total_annual:<19.2f}"
    )

print(subdivider)

#
# Trend Direction
#

initial_total = totals[0]
latest_total = totals[-1]

delta = (
    latest_total -
    initial_total
)

print(
    f"{'INITIAL FLOW':<25}"
    f"${initial_total:,.2f}"
)

print(
    f"{'LATEST FLOW':<25}"
    f"${latest_total:,.2f}"
)

print(
    f"{'TOTAL DELTA':<25}"
    f"${delta:,.2f}"
)

print(subdivider)

#
# Runtime Trend Assessment
#

if delta > 0:

    trend_status = (
        "POSITIVE GROWTH"
    )

elif delta < 0:

    trend_status = (
        "NEGATIVE DECLINE"
    )

else:

    trend_status = (
        "STABLE FLOW"
    )

print(
    f"{'TREND STATUS':<25}"
    f"{trend_status}"
)

print(divider)
print("END INCOME TREND")
print(divider)
