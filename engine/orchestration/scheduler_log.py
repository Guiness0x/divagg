import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SCHEDULER_LOG = (
    BASE_DIR /
    "logs" /
    "schedulers" /
    "scheduler_runtime_log.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: SCHEDULER LOG")
print(divider)

if not SCHEDULER_LOG.exists():

    print("\n[ERROR] Scheduler runtime log missing.")
    raise SystemExit(1)

with open(
    SCHEDULER_LOG,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nSCHEDULER EXECUTION HISTORY:\n")

print(subdivider)

print(
    f"{'TIMESTAMP':<36}"
    f"{'SCHEDULER':<24}"
    f"{'RESULT':<18}"
)

print(subdivider)

for row in rows[-10:]:

    timestamp = (
        row.get(
            "timestamp"
        )
        or "UNKNOWN"
    )

    scheduler = (
        row.get(
            "scheduler"
        )
        or "UNKNOWN"
    )

    result = (
        row.get(
            "result"
        )
        or "UNKNOWN"
    )

    print(
        f"{timestamp:<36}"
        f"{scheduler:<24}"
        f"{result:<18}"
    )

print(subdivider)

print(
    f"{'TOTAL LOG ENTRIES':<30}"
    f"{len(rows)}"
)

print(divider)
print("END SCHEDULER LOG")
print(divider)
