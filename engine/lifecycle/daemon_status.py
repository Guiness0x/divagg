import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DAEMON_REGISTRY = (
    BASE_DIR /
    "data" /
    "daemons" /
    "daemon_registry.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: DAEMON STATUS")
print(divider)

if not DAEMON_REGISTRY.exists():

    print("\n[ERROR] Daemon registry missing.")
    raise SystemExit(1)

with open(
    DAEMON_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nDAEMON TOPOLOGY:\n")

print(subdivider)

print(
    f"{'DAEMON':<24}"
    f"{'STATUS':<14}"
    f"{'MODE':<16}"
    f"{'PURPOSE':<36}"
)

print(subdivider)

planned_daemons = 0
active_daemons = 0
inactive_daemons = 0

for row in rows:

    daemon_name = (
        row.get(
            "daemon_name"
        )
        or "UNKNOWN"
    )

    status = (
        row.get(
            "status"
        )
        or "UNKNOWN"
    )

    mode = (
        row.get(
            "mode"
        )
        or "UNKNOWN"
    )

    purpose = (
        row.get(
            "purpose"
        )
        or "UNKNOWN"
    )

    if status == "planned":

        planned_daemons += 1

    elif status == "active":

        active_daemons += 1

    else:

        inactive_daemons += 1

    print(
        f"{daemon_name:<24}"
        f"{status:<14}"
        f"{mode:<16}"
        f"{purpose:<36}"
    )

print(subdivider)

print(
    f"{'PLANNED DAEMONS':<30}"
    f"{planned_daemons}"
)

print(
    f"{'ACTIVE DAEMONS':<30}"
    f"{active_daemons}"
)

print(
    f"{'INACTIVE DAEMONS':<30}"
    f"{inactive_daemons}"
)

print(subdivider)

#
# Runtime Assessment
#

if active_daemons == 0:

    runtime_status = (
        "DAEMONIZATION PREP ACTIVE"
    )

elif active_daemons < 3:

    runtime_status = (
        "PARTIAL DAEMON COVERAGE"
    )

else:

    runtime_status = (
        "DAEMON LAYER ACTIVE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END DAEMON STATUS")
print(divider)
