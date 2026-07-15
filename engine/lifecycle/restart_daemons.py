import csv

from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DAEMON_LIFECYCLE = (
    BASE_DIR /
    "data" /
    "daemons" /
    "daemon_lifecycle.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: RESTART DAEMONS")
print(divider)

if not DAEMON_LIFECYCLE.exists():

    print("\n[ERROR] Daemon lifecycle registry missing.")
    raise SystemExit(1)

with open(
    DAEMON_LIFECYCLE,
    newline="",
    encoding="utf-8"
) as csvfile:

    reader = csv.DictReader(
        csvfile
    )

    fieldnames = reader.fieldnames
    rows = list(reader)

timestamp = datetime.now(
    timezone.utc
).isoformat()

restart_total = 0

for row in rows:

    state = (
        row.get(
            "lifecycle_state"
        )
        or ""
    )

    if state == "running":

        current_count = int(
            row.get(
                "restart_count"
            )
            or 0
        )

        row["restart_count"] = str(
            current_count + 1
        )

        row["last_restart"] = timestamp
        row["last_started"] = timestamp

        restart_total += 1

with open(
    DAEMON_LIFECYCLE,
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

print("\nDAEMON RESTART ANALYSIS:\n")

print(subdivider)

print(
    f"{'RESTARTED DAEMONS':<30}"
    f"{restart_total}"
)

print(
    f"{'RESTART TIMESTAMP':<30}"
    f"{timestamp}"
)

print(subdivider)

if restart_total == 0:

    runtime_status = (
        "NO RUNNING DAEMONS"
    )

else:

    runtime_status = (
        "DAEMON RESTART COMPLETE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END RESTART DAEMONS")
print(divider)
