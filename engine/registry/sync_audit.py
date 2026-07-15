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
print("DIVAGG :: SYNC AUDIT")
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
# Synchronization Audit
#

print("\nSYNCHRONIZATION AUDIT:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'FEED YIELD':<15}"
    f"{'REGISTRY YIELD':<18}"
    f"{'STATUS':<18}"
)

print(subdivider)

matched_entries = 0
drift_entries = 0

for row in spreadsheet_rows:

    ticker = row.get(
        "ticker"
    )

    if not ticker:

        continue

    feed_yield = (
        row.get(
            "dividend_yield"
        )
        or "0.00"
    )

    registry_yield = (
        registry_map.get(
            ticker,
            {}
        ).get(
            "dividend_yield",
            "0.00"
        )
    )

    if feed_yield == registry_yield:

        status = "SYNCHRONIZED"
        matched_entries += 1

    else:

        status = "DRIFT DETECTED"
        drift_entries += 1

    print(
        f"{ticker:<10}"
        f"{feed_yield + '%':<15}"
        f"{registry_yield + '%':<18}"
        f"{status:<18}"
    )

print(subdivider)

print(
    f"{'MATCHED ENTRIES':<30}"
    f"{matched_entries}"
)

print(
    f"{'DRIFT ENTRIES':<30}"
    f"{drift_entries}"
)

print(subdivider)

#
# Runtime Assessment
#

if drift_entries == 0:

    runtime_status = (
        "SYNC VERIFIED"
    )

elif drift_entries <= 3:

    runtime_status = (
        "MINOR DRIFT"
    )

else:

    runtime_status = (
        "MAJOR DRIFT DETECTED"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END SYNC AUDIT")
print(divider)
