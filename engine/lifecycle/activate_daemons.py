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

EVENT_LOG = (
    BASE_DIR /
    "logs" /
    "runtime_events" /
    "runtime_events.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: ACTIVATE DAEMONS")
print(divider)

if not DAEMON_LIFECYCLE.exists():
    print("\n[ERROR] Daemon lifecycle registry missing.")
    raise SystemExit(1)

with open(
    DAEMON_LIFECYCLE,
    newline="",
    encoding="utf-8"
) as csvfile:

    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    rows = list(reader)

timestamp = datetime.now(
    timezone.utc
).isoformat()

activated = 0
event_rows = []

for row in rows:

    state = (
        row.get(
            "lifecycle_state"
        )
        or ""
    )

    if state != "running":

        row["lifecycle_state"] = "running"
        row["last_started"] = timestamp

        activated += 1

        event_rows.append({
            "timestamp": timestamp,
            "event_type": "activation",
            "daemon": row["daemon_name"],
            "status": "running"
        })

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

if event_rows:

    with open(
        EVENT_LOG,
        "a",
        newline="",
        encoding="utf-8"
    ) as logfile:

        writer = csv.DictWriter(
            logfile,
            fieldnames=[
                "timestamp",
                "event_type",
                "daemon",
                "status"
            ]
        )

        writer.writerows(event_rows)

print("\nDAEMON ACTIVATION:\n")

print(subdivider)

print(
    f"{'ACTIVATED DAEMONS':<30}"
    f"{activated}"
)

print(
    f"{'ACTIVATION TIMESTAMP':<30}"
    f"{timestamp}"
)

print(subdivider)

if activated == 0:

    runtime_status = (
        "DAEMONS ALREADY ACTIVE"
    )

else:

    runtime_status = (
        "DAEMON LAYER ACTIVATED"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END ACTIVATE DAEMONS")
print(divider)
