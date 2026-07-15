import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

EVENT_LOG = (
    BASE_DIR /
    "logs" /
    "runtime_events" /
    "runtime_events.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: EVENT LOG")
print(divider)

if not EVENT_LOG.exists():

    print("\n[ERROR] Runtime event log missing.")
    raise SystemExit(1)

with open(
    EVENT_LOG,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nRUNTIME EVENT HISTORY:\n")

print(subdivider)

print(
    f"{'TIMESTAMP':<36}"
    f"{'EVENT':<18}"
    f"{'DAEMON':<24}"
    f"{'STATUS':<18}"
)

print(subdivider)

for row in rows[-20:]:

    print(
        f"{row['timestamp']:<36}"
        f"{row['event_type']:<18}"
        f"{row['daemon']:<24}"
        f"{row['status']:<18}"
    )

print(subdivider)

print(
    f"{'TOTAL EVENTS':<30}"
    f"{len(rows)}"
)

print(divider)
print("END EVENT LOG")
print(divider)
