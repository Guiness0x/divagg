import csv
from pathlib import Path

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
print("DIVAGG :: LIVE REGISTRY")
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

print("\nLIVE REGISTRY ENTRIES:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'ASSET TYPE':<20}"
    f"{'PAYOUT':<15}"
    f"{'SOURCE':<20}"
)

print(subdivider)

for row in rows:

    ticker = (
        row.get("ticker")
        or "UNKNOWN"
    )

    asset_type = (
        row.get("asset_type")
        or "UNKNOWN"
    )

    payout_frequency = (
        row.get("payout_frequency")
        or "UNKNOWN"
    )

    source = (
        row.get("source")
        or "UNSET"
    )

    print(
        f"{ticker:<10}"
        f"{asset_type:<20}"
        f"{payout_frequency:<15}"
        f"{source:<20}"
    )

print(subdivider)

print(
    f"{'TOTAL LIVE ENTRIES':<30}"
    f"{len(rows)}"
)

print(divider)
print("END LIVE REGISTRY")
print(divider)
