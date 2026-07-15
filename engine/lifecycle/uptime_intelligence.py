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
print("DIVAGG :: UPTIME INTELLIGENCE")
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

print("\nSERVICE UPTIME ANALYSIS:\n")

print(subdivider)

print(
    f"{'DAEMON':<24}"
    f"{'STATE':<16}"
    f"{'UPTIME':<24}"
    f"{'STATUS':<18}"
)

print(subdivider)

running_services = 0
stable_services = 0

now = datetime.now(
    timezone.utc
)

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

    last_started = (
        row.get(
            "last_started"
        )
        or ""
    )

    uptime_display = "not_running"
    status = "INACTIVE"

    if state == "running" and last_started:

        try:

            started = datetime.fromisoformat(
                last_started
            )

            uptime_delta = (
                now - started
            )

            total_seconds = int(
                uptime_delta.total_seconds()
            )

            hours = (
                total_seconds // 3600
            )

            minutes = (
                (total_seconds % 3600) // 60
            )

            seconds = (
                total_seconds % 60
            )

            uptime_display = (
                f"{hours}h {minutes}m {seconds}s"
            )

            running_services += 1
            stable_services += 1

            status = "STABLE"

        except Exception:

            uptime_display = "invalid_timestamp"
            status = "ERROR"

    print(
        f"{daemon_name:<24}"
        f"{state:<16}"
        f"{uptime_display:<24}"
        f"{status:<18}"
    )

print(subdivider)

print(
    f"{'RUNNING SERVICES':<30}"
    f"{running_services}"
)

print(
    f"{'STABLE SERVICES':<30}"
    f"{stable_services}"
)

print(subdivider)

#
# Runtime Assessment
#

if stable_services == 0:

    runtime_status = (
        "NO ACTIVE SERVICE UPTIME"
    )

elif stable_services < len(rows):

    runtime_status = (
        "PARTIAL SERVICE STABILITY"
    )

else:

    runtime_status = (
        "ALL SERVICES STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END UPTIME INTELLIGENCE")
print(divider)
