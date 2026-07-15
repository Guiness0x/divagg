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

HISTORY_DIR = (
    BASE_DIR /
    "history_runtime"
)

HISTORY_DIR.mkdir(
    exist_ok=True
)

divider = "=" * 60
subdivider = "-" * 60

ALLOCATION_PER_ASSET = 10000

print(divider)
print("DIVAGG :: HISTORICAL STATE")
print(divider)

if not LIVE_REGISTRY.exists():

    print("\n[ERROR] Live registry missing.")
    raise SystemExit(1)

timestamp = datetime.now(
    timezone.utc
).strftime(
    "%Y-%m-%d_%H-%M-%S"
)

history_file = (
    HISTORY_DIR /
    f"historical_state_{timestamp}.csv"
)

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

        #
        # Runtime Projection Snapshot
        #

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

        monthly_income = (
            annual_income / 12
        )

        row[
            "projected_annual_income"
        ] = f"{annual_income:.2f}"

        row[
            "projected_monthly_income"
        ] = f"{monthly_income:.2f}"

        row[
            "historical_timestamp"
        ] = timestamp

        rows.append(row)

#
# Expanded Historical Schema
#

historical_fields = (
    fieldnames +
    [
        "projected_annual_income",
        "projected_monthly_income",
        "historical_timestamp"
    ]
)

with open(
    history_file,
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=historical_fields
    )

    writer.writeheader()

    writer.writerows(rows)

print("\nHISTORICAL SNAPSHOT CREATED:\n")

print(subdivider)

print(
    f"{'SNAPSHOT FILE':<20}"
    f"{history_file}"
)

print(subdivider)

print(
    f"{'SNAPSHOT ENTRIES':<20}"
    f"{len(rows)}"
)

print(
    f"{'SNAPSHOT TIMESTAMP':<20}"
    f"{timestamp}"
)

print(divider)
print("END HISTORICAL STATE")
print(divider)
