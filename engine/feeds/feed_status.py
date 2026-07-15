import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FEED_SOURCES = (
    BASE_DIR /
    "data" /
    "feeds" /
    "feed_sources.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: FEED STATUS")
print(divider)

if not FEED_SOURCES.exists():

    print("\n[ERROR] Feed sources file missing.")
    raise SystemExit(1)

with open(
    FEED_SOURCES,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nLIVE FEED SOURCES:\n")

print(subdivider)

print(
    f"{'SOURCE':<22}"
    f"{'STATUS':<12}"
    f"{'TYPE':<18}"
    f"{'NOTES':<35}"
)

print(subdivider)

for row in rows:

    print(
        f"{(row.get('source_name') or 'UNKNOWN'):<22}"
        f"{(row.get('status') or 'UNKNOWN'):<12}"
        f"{(row.get('feed_type') or 'UNKNOWN'):<18}"
        f"{(row.get('notes') or ''):<35}"
    )

print(subdivider)

print(
    f"{'TOTAL SOURCES':<30}"
    f"{len(rows)}"
)

print(divider)
print("END FEED STATUS")
print(divider)
