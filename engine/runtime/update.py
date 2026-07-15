import csv
from pathlib import Path
from datetime import datetime
import shutil
import sys

INPUT_FILE = Path("../data/portfolio.csv")
SNAPSHOT_DIR = Path("../snapshots")

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

UPDATABLE_FIELDS = {
    "shares",
    "dividend",
    "frequency"
}

divider = "=" * 60

print(divider)
print("DIVAGG :: UPDATE POSITION")
print(divider)

if not INPUT_FILE.exists():

    print("[ERROR] portfolio.csv not found.")
    sys.exit(1)

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

ticker_to_update = input(
    "\nTicker to update : "
).strip().upper()

matching_row = None

for row in rows:

    if row["ticker"].upper() == ticker_to_update:
        matching_row = row
        break

if not matching_row:

    print(f"\n[ERROR] Ticker not found: {ticker_to_update}")
    sys.exit(1)

print("\nCURRENT POSITION:\n")

print(
    f"{matching_row['ticker']} | "
    f"{matching_row['shares']} shares | "
    f"{matching_row['dividend']} dividend | "
    f"{matching_row['frequency']}"
)

#
# Field Selection
#

field_to_update = input(
    "\nField to update "
    "(shares/dividend/frequency) : "
).strip().lower()

if field_to_update not in UPDATABLE_FIELDS:

    print("\n[ERROR] Invalid field.")
    sys.exit(1)

new_value = input(
    f"\nNew value for {field_to_update} : "
).strip()

#
# Validation
#

try:

    if field_to_update == "shares":

        value = float(new_value)

        if value < 0:
            raise ValueError

        new_value = str(value)

    elif field_to_update == "dividend":

        value = float(new_value)

        if value < 0:
            raise ValueError

        new_value = str(value)

    elif field_to_update == "frequency":

        if new_value.lower() not in VALID_FREQUENCIES:
            raise ValueError

        new_value = new_value.lower()

except Exception:

    print("\n[ERROR] Invalid update value.")
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
# Apply Update
#

matching_row[field_to_update] = new_value

confirmation = input(
    "\nConfirm update? (yes/no) : "
).strip().lower()

if confirmation != "yes":

    print("\n[INFO] Update cancelled.")
    sys.exit(0)

#
# Safe Rewrite
#

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

        for row in rows:
            writer.writerow(row)

    print("\n[SUCCESS] Position updated.")

except Exception as error:

    print(f"\n[ERROR] Failed rewrite :: {error}")
    sys.exit(1)

print(f"\n{divider}")
print("END UPDATE")
print(divider)
