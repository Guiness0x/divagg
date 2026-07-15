import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SPREADSHEET_FEED = (
    BASE_DIR /
    "data" /
    "feeds" /
    "spreadsheets" /
    "spreadsheet_feed.csv"
)

LIVE_REGISTRY = (
    BASE_DIR /
    "data" /
    "live" /
    "live_registry.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: SYNC SPREADSHEET")
print(divider)

if not SPREADSHEET_FEED.exists():

    print("\n[ERROR] Spreadsheet feed missing.")
    raise SystemExit(1)

if not LIVE_REGISTRY.exists():

    print("\n[ERROR] Live registry missing.")
    raise SystemExit(1)

#
# Load Spreadsheet Feed
#

with open(
    SPREADSHEET_FEED,
    newline="",
    encoding="utf-8"
) as csvfile:

    spreadsheet_rows = list(
        csv.DictReader(csvfile)
    )

#
# Load Live Registry
#

with open(
    LIVE_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    registry_rows = list(
        csv.DictReader(csvfile)
    )

registry_map = {}

for row in registry_rows:

    ticker = row.get(
        "ticker"
    )

    if ticker:

        registry_map[
            ticker
        ] = row

#
# Synchronization
#

updated_entries = 0

for row in spreadsheet_rows:

    ticker = row.get(
        "ticker"
    )

    if not ticker:

        continue

    if ticker not in registry_map:

        continue

    registry_map[
        ticker
    ][
        "dividend_yield"
    ] = row.get(
        "dividend_yield",
        ""
    )

    registry_map[
        ticker
    ][
        "payout_frequency"
    ] = row.get(
        "payout_frequency",
        ""
    )

    registry_map[
        ticker
    ][
        "share_price"
    ] = row.get(
        "share_price",
        ""
    )

    registry_map[
        ticker
    ][
        "source"
    ] = "spreadsheet_feed"

    updated_entries += 1

#
# Write Updated Registry
#

fieldnames = registry_rows[0].keys()

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

    for row in registry_map.values():

        writer.writerow(row)

#
# Runtime Output
#

print("\nSPREADSHEET SYNCHRONIZATION:\n")

print(subdivider)

print(
    f"{'UPDATED ENTRIES':<30}"
    f"{updated_entries}"
)

print(
    f"{'SYNCHRONIZATION SOURCE':<30}"
    f"spreadsheet_feed"
)

print(
    f"{'LIVE REGISTRY UPDATED':<30}"
    f"yes"
)

print(subdivider)

if updated_entries == 0:

    runtime_status = (
        "NO SYNCHRONIZATION"
    )

elif updated_entries < 5:

    runtime_status = (
        "PARTIAL SYNCHRONIZATION"
    )

else:

    runtime_status = (
        "SYNCHRONIZATION STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END SYNC SPREADSHEET")
print(divider)
