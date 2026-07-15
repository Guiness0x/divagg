import csv
import sys
from pathlib import Path

from utils.loader import (
    ACTIVE_PORTFOLIO
)

SNAPSHOT_DIR = Path("../snapshots")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SNAPSHOT COMPARISON")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

#
# Discover Snapshots
#

snapshots = sorted(
    SNAPSHOT_DIR.glob(
        f"{ACTIVE_PORTFOLIO}_snapshot_*.csv"
    ),
    reverse=True
)

if len(snapshots) < 2:

    print(
        "\n[ERROR] At least two snapshots required."
    )

    sys.exit(1)

print("\nAVAILABLE SNAPSHOTS:\n")

for index, snapshot in enumerate(snapshots, start=1):

    print(
        f"{index}. "
        f"{snapshot.name}"
    )

#
# Select Snapshots
#

selection_one = input(
    "\nFirst snapshot number : "
).strip()

selection_two = input(
    "Second snapshot number : "
).strip()

try:

    first_snapshot = snapshots[
        int(selection_one) - 1
    ]

    second_snapshot = snapshots[
        int(selection_two) - 1
    ]

except Exception:

    print("\n[ERROR] Invalid selection.")
    sys.exit(1)

#
# Load Snapshot Data
#

def load_snapshot(snapshot_file):

    positions = {}

    with open(snapshot_file, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row["ticker"]

            positions[ticker] = {
                "shares": row["shares"],
                "dividend": row["dividend"],
                "frequency": row["frequency"]
            }

    return positions

try:

    first_positions = load_snapshot(
        first_snapshot
    )

    second_positions = load_snapshot(
        second_snapshot
    )

except Exception as error:

    print(
        f"\n[ERROR] Snapshot load failed :: "
        f"{error}"
    )

    sys.exit(1)

#
# Compare
#

added = []
removed = []
updated = []

#
# Added / Updated
#

for ticker, data in second_positions.items():

    if ticker not in first_positions:

        added.append(ticker)

    elif data != first_positions[ticker]:

        updated.append(ticker)

#
# Removed
#

for ticker in first_positions:

    if ticker not in second_positions:

        removed.append(ticker)

#
# Output
#

print("\nSNAPSHOT DIFFERENCES:\n")

print(subdivider)

print("\nADDED:\n")

if added:

    for ticker in added:

        print(f"- {ticker}")

else:

    print("None")

print("\nUPDATED:\n")

if updated:

    for ticker in updated:

        print(f"- {ticker}")

else:

    print("None")

print("\nREMOVED:\n")

if removed:

    for ticker in removed:

        print(f"- {ticker}")

else:

    print("None")

print(subdivider)

print(divider)
print("END SNAPSHOT COMPARISON")
print(divider)
