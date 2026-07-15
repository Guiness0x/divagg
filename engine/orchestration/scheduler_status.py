import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SCHEDULER_REGISTRY = (
    BASE_DIR /
    "data" /
    "schedulers" /
    "scheduler_registry.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: SCHEDULER STATUS")
print(divider)

if not SCHEDULER_REGISTRY.exists():

    print("\n[ERROR] Scheduler registry missing.")
    raise SystemExit(1)

with open(
    SCHEDULER_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nSCHEDULER TOPOLOGY:\n")

print(subdivider)

print(
    f"{'SCHEDULER':<24}"
    f"{'TYPE':<14}"
    f"{'STATUS':<12}"
    f"{'FREQUENCY':<14}"
    f"{'SOURCE':<20}"
)

print(subdivider)

active_schedulers = 0
planned_schedulers = 0
disabled_schedulers = 0

for row in rows:

    scheduler_name = (
        row.get(
            "scheduler_name"
        )
        or "UNKNOWN"
    )

    schedule_type = (
        row.get(
            "schedule_type"
        )
        or "UNKNOWN"
    )

    status = (
        row.get(
            "status"
        )
        or "UNKNOWN"
    )

    frequency = (
        row.get(
            "frequency"
        )
        or "UNKNOWN"
    )

    source = (
        row.get(
            "source"
        )
        or "UNKNOWN"
    )

    if status == "active":

        active_schedulers += 1

    elif status == "planned":

        planned_schedulers += 1

    elif status == "disabled":

        disabled_schedulers += 1

    print(
        f"{scheduler_name:<24}"
        f"{schedule_type:<14}"
        f"{status:<12}"
        f"{frequency:<14}"
        f"{source:<20}"
    )

print(subdivider)

print(
    f"{'ACTIVE SCHEDULERS':<30}"
    f"{active_schedulers}"
)

print(
    f"{'PLANNED SCHEDULERS':<30}"
    f"{planned_schedulers}"
)

print(
    f"{'DISABLED SCHEDULERS':<30}"
    f"{disabled_schedulers}"
)

print(subdivider)

#
# Runtime Assessment
#

if active_schedulers == 0:

    runtime_status = (
        "NO ACTIVE SCHEDULERS"
    )

elif disabled_schedulers >= 2:

    runtime_status = (
        "PARTIAL CADENCE COVERAGE"
    )

else:

    runtime_status = (
        "SCHEDULER LAYER STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END SCHEDULER STATUS")
print(divider)
