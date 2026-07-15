import csv
from pathlib import Path
from datetime import datetime
import shutil
import sys

INPUT_FILE = Path("../data/portfolio.csv")
SNAPSHOT_DIR = Path("../snapshots")

divider = "=" * 60

print(divider)
print("DIVAGG :: REMOVE POSITION")
print(divider)

if not INPUT_FILE.exists():

    print("[ERROR] portfolio.csv not found.")
    sys.exit(1)

#
# Automatic Snapshot
#

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

snapshot_path = (
    SNAPSHOT_DIR /
    f"portfolio_snapshot_{timestamp}.csv"
)

shutil.copy2(INPUT_FILE, snapshot_path)

print("\n[INFO] Automatic snapshot created:")
print(snapshot_path)

#
# Load Portfolio
#

rows = []

try:

    with open(INPUT_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            rows.append(row)

except Exception as error:

    print(f"[ERROR] Failed to load portfolio :: {error}")
    sys.exit(1)

#
# User Input
#

ticker_to_remove = input(
    "\nTicker to remove : "
).strip().upper()

matching_rows = [
    row for row in rows
    if row["ticker"].upper() == ticker_to_remove
]

if not matching_rows:

    print(f"\n[ERROR] Ticker not found: {ticker_to_remove}")
    sys.exit(1)

print("\nMATCH FOUND:\n")

for row in matching_rows:

    print(
        f"{row['ticker']} | "
        f"{row['shares']} shares | "
        f"{row['dividend']} dividend | "
        f"{row['frequency']}"
    )

confirmation = input(
    "\nConfirm removal? (yes/no) : "
).strip().lower()

if confirmation != "yes":

    print("\n[INFO] Removal cancelled.")
    sys.exit(0)

#
# Safe Rewrite
#

remaining_rows = [
    row for row in rows
    if row["ticker"].upper() != ticker_to_remove
]

try:

    with open(INPUT_FILE, "w", newline='') as csvfile:

        fieldnames = [
            "ticker",
            "shares",
            "dividend",
            "frequency"
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in remaining_rows:
            writer.writerow(row)

    print(f"\n[SUCCESS] Removed ticker:")
    print(ticker_to_remove)

except Exception as error:

    print(f"[ERROR] Failed rewrite :: {error}")
    sys.exit(1)

print(f"\n{divider}")
print("END REMOVE POSITION")
print(divider)
