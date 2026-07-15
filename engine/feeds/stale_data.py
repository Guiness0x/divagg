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

STALE_THRESHOLD_DAYS = 7

print(divider)
print("DIVAGG :: STALE DATA")
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

print("\nSTALE DATA ANALYSIS:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'LAST UPDATED':<30}"
    f"{'STATUS':<20}"
)

print(subdivider)

current_time = datetime.now(
    timezone.utc
)

stale_count = 0

for row in rows:

    ticker = (
        row.get("ticker")
        or "UNKNOWN"
    )

    last_updated = (
        row.get("last_updated")
    )

    if not last_updated:

        status = "MISSING"

        stale_count += 1

        print(
            f"{ticker:<10}"
            f"{'UNSET':<30}"
            f"{status:<20}"
        )

        continue

    try:

        parsed_time = datetime.fromisoformat(
            last_updated
        )

        age = (
            current_time -
            parsed_time.astimezone(
                timezone.utc
            )
        ).days

        if age > STALE_THRESHOLD_DAYS:

            status = "STALE"

            stale_count += 1

        else:

            status = "FRESH"

    except Exception:

        status = "INVALID"

        stale_count += 1

    print(
        f"{ticker:<10}"
        f"{last_updated:<30}"
        f"{status:<20}"
    )

print(subdivider)

print(
    f"{'TOTAL ENTRIES':<30}"
    f"{len(rows)}"
)

print(
    f"{'STALE/MISSING':<30}"
    f"{stale_count}"
)

print(divider)
print("END STALE DATA")
print(divider)
