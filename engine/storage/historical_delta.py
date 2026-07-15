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
print("DIVAGG :: HISTORICAL DELTA")
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

previous_snapshot = history_files[-2]
current_snapshot = history_files[-1]

print("\nRUNTIME DELTA ANALYSIS:\n")

print(subdivider)

print(
    f"{'PREVIOUS SNAPSHOT':<25}"
    f"{previous_snapshot.name}"
)

print(
    f"{'CURRENT SNAPSHOT':<25}"
    f"{current_snapshot.name}"
)

print(subdivider)

#
# Load Snapshot Data
#

def load_snapshot(path):

    snapshot_data = {}

    with open(
        path,
        newline="",
        encoding="utf-8"
    ) as csvfile:

        reader = csv.DictReader(
            csvfile
        )

        for row in reader:

            ticker = (
                row.get("ticker")
            )

            if not ticker:

                continue

            snapshot_data[
                ticker
            ] = row

    return snapshot_data

previous_data = load_snapshot(
    previous_snapshot
)

current_data = load_snapshot(
    current_snapshot
)

#
# Delta Analysis
#

changes_detected = 0

print(
    f"{'TICKER':<10}"
    f"{'PREVIOUS':<15}"
    f"{'CURRENT':<15}"
    f"{'DELTA':<15}"
)

print(subdivider)

for ticker in current_data:

    current_income = float(
        current_data[
            ticker
        ].get(
            "projected_annual_income",
            0.0
        )
    )

    previous_income = float(
        previous_data.get(
            ticker,
            {}
        ).get(
            "projected_annual_income",
            0.0
        )
    )

    delta = (
        current_income -
        previous_income
    )

    if delta != 0:

        changes_detected += 1

    print(
        f"{ticker:<10}"
        f"${previous_income:<14.2f}"
        f"${current_income:<14.2f}"
        f"${delta:<14.2f}"
    )

print(subdivider)

print(
    f"{'CHANGES DETECTED':<25}"
    f"{changes_detected}"
)

#
# Runtime Assessment
#

if changes_detected == 0:

    delta_status = (
        "STABLE STATE"
    )

elif changes_detected <= 3:

    delta_status = (
        "MINOR EVOLUTION"
    )

else:

    delta_status = (
        "MAJOR EVOLUTION"
    )

print(
    f"{'DELTA STATUS':<25}"
    f"{delta_status}"
)

print(divider)
print("END HISTORICAL DELTA")
print(divider)
