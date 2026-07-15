import csv
from pathlib import Path

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
print("DIVAGG :: DAEMON LIFECYCLE")
print(divider)

if not DAEMON_LIFECYCLE.exists():

    print("\n[ERROR] Daemon lifecycle registry missing.")
    raise SystemExit(1)

with open(
    DAEMON_LIFECYCLE,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(csv.DictReader(csvfile))

print("\nDAEMON LIFECYCLE STATE:\n")
print(subdivider)

print(
    f"{'DAEMON':<24}"
    f"{'STATE':<18}"
    f"{'LAST STARTED':<24}"
    f"{'POLICY':<12}"
)

print(subdivider)

not_started = 0
running = 0
stopped = 0

for row in rows:

    daemon_name = row.get("daemon_name") or "UNKNOWN"
    state = row.get("lifecycle_state") or "UNKNOWN"
    last_started = row.get("last_started") or "never"
    policy = row.get("restart_policy") or "UNKNOWN"

    if state == "not_started":
        not_started += 1
    elif state == "running":
        running += 1
    elif state == "stopped":
        stopped += 1

    print(
        f"{daemon_name:<24}"
        f"{state:<18}"
        f"{last_started:<24}"
        f"{policy:<12}"
    )

print(subdivider)

print(f"{'RUNNING DAEMONS':<30}{running}")
print(f"{'NOT STARTED':<30}{not_started}")
print(f"{'STOPPED DAEMONS':<30}{stopped}")

print(subdivider)

if running == 0:
    runtime_status = "DAEMON LIFECYCLE READY"
elif running < len(rows):
    runtime_status = "PARTIAL DAEMON ACTIVITY"
else:
    runtime_status = "ALL DAEMONS RUNNING"

print(f"{'RUNTIME STATUS':<30}{runtime_status}")

print(divider)
print("END DAEMON LIFECYCLE")
print(divider)
