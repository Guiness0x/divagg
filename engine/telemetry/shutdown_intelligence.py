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
print("DIVAGG :: SHUTDOWN INTELLIGENCE")
print(divider)

if not DAEMON_LIFECYCLE.exists():

    print("\n[ERROR] Daemon lifecycle registry missing.")
    raise SystemExit(1)

with open(
    DAEMON_LIFECYCLE,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nSHUTDOWN STATE ANALYSIS:\n")

print(subdivider)

print(
    f"{'DAEMON':<24}"
    f"{'STATE':<16}"
    f"{'LAST STOPPED':<36}"
    f"{'STATUS':<18}"
)

print(subdivider)

stopped_services = 0
running_services = 0

for row in rows:

    daemon_name = (
        row.get(
            "daemon_name"
        )
        or "UNKNOWN"
    )

    state = (
        row.get(
            "lifecycle_state"
        )
        or "UNKNOWN"
    )

    last_stopped = (
        row.get(
            "last_stopped"
        )
        or "never"
    )

    if state == "stopped":

        stopped_services += 1
        status = "CONTROLLED STOP"

    elif state == "running":

        running_services += 1
        status = "STILL RUNNING"

    else:

        status = "NOT ACTIVE"

    print(
        f"{daemon_name:<24}"
        f"{state:<16}"
        f"{last_stopped:<36}"
        f"{status:<18}"
    )

print(subdivider)

print(
    f"{'STOPPED SERVICES':<30}"
    f"{stopped_services}"
)

print(
    f"{'RUNNING SERVICES':<30}"
    f"{running_services}"
)

print(
    f"{'TOTAL DAEMONS':<30}"
    f"{len(rows)}"
)

print(subdivider)

if stopped_services == len(rows):

    runtime_status = (
        "SHUTDOWN STATE CLEAN"
    )

elif running_services > 0:

    runtime_status = (
        "PARTIAL SHUTDOWN"
    )

else:

    runtime_status = (
        "NO ACTIVE DAEMONS"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END SHUTDOWN INTELLIGENCE")
print(divider)
