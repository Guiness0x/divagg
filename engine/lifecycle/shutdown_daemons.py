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
print("DIVAGG :: SHUTDOWN DAEMONS")
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

timestamp = datetime.now(timezone.utc).isoformat()

shutdown_total = 0

for row in rows:
    state = row.get("lifecycle_state") or ""

    if state == "running":
        row["lifecycle_state"] = "stopped"
        row["last_stopped"] = timestamp
        shutdown_total += 1

with open(
    DAEMON_LIFECYCLE,
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("\nDAEMON SHUTDOWN:\n")
print(subdivider)

print(f"{'SHUTDOWN DAEMONS':<30}{shutdown_total}")
print(f"{'SHUTDOWN TIMESTAMP':<30}{timestamp}")

print(subdivider)

if shutdown_total == 0:
    runtime_status = "NO RUNNING DAEMONS"
else:
    runtime_status = "DAEMON SHUTDOWN COMPLETE"

print(f"{'RUNTIME STATUS':<30}{runtime_status}")

print(divider)
print("END SHUTDOWN DAEMONS")
print(divider)
