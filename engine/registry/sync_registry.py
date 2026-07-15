import csv

from pathlib import Path
from datetime import datetime
from datetime import timezone

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LIVE_REGISTRY = (
    BASE_DIR /
    "data" /
    "live" /
    "live_registry.csv"
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SYNC REGISTRY")
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

    fieldnames = reader.fieldnames

    for row in reader:

        if not row:

            continue

        ticker = (
            row.get("ticker")
        )

        if not ticker:

            continue

        rows.append(row)

current_timestamp = (
    datetime.now(
        timezone.utc
    ).isoformat()
)

updated_count = 0

for row in rows:

    row["last_updated"] = current_timestamp

    source = (
        row.get("source")
        or ""
    ).strip()

    if (
        source == ""
        or
        source == "manual_seed"
        or
        source == "UNSET"
    ):

        row["source"] = "runtime_sync"

    updated_count += 1

with open(
    LIVE_REGISTRY,
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(rows)

print("\nREGISTRY SYNCHRONIZATION:\n")

print(subdivider)

print(
    f"{'UPDATED ENTRIES':<30}"
    f"{updated_count}"
)

print(
    f"{'SYNC TIMESTAMP':<30}"
    f"{current_timestamp}"
)

print(subdivider)

print(divider)
print("END SYNC REGISTRY")
print(divider)
