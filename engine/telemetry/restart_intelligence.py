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
print("DIVAGG :: RESTART INTELLIGENCE")
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

print("\nRESTART STABILITY ANALYSIS:\n")

print(subdivider)

print(
    f"{'DAEMON':<24}"
    f"{'RESTARTS':<14}"
    f"{'LAST RESTART':<36}"
    f"{'STATUS':<18}"
)

print(subdivider)

stable_services = 0

for row in rows:

    daemon_name = (
        row.get(
            "daemon_name"
        )
        or "UNKNOWN"
    )

    restart_count = int(
        row.get(
            "restart_count"
        )
        or 0
    )

    last_restart = (
        row.get(
            "last_restart"
        )
        or "never"
    )

    if restart_count <= 3:

        status = "STABLE"
        stable_services += 1

    elif restart_count <= 5:

        status = "WATCH"

    else:

        status = "UNSTABLE"

    print(
        f"{daemon_name:<24}"
        f"{restart_count:<14}"
        f"{last_restart:<36}"
        f"{status:<18}"
    )

print(subdivider)

print(
    f"{'STABLE SERVICES':<30}"
    f"{stable_services}"
)

print(
    f"{'TOTAL DAEMONS':<30}"
    f"{len(rows)}"
)

print(subdivider)

if stable_services == len(rows):

    runtime_status = (
        "RESTART STABILITY NORMAL"
    )

elif stable_services > 0:

    runtime_status = (
        "PARTIAL RESTART STABILITY"
    )

else:

    runtime_status = (
        "RESTART INSTABILITY DETECTED"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END RESTART INTELLIGENCE")
print(divider)
