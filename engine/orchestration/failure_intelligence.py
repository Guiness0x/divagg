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
print("DIVAGG :: FAILURE INTELLIGENCE")
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

print("\nORCHESTRATION FAILURE ANALYSIS:\n")

print(subdivider)

print(
    f"{'SCHEDULER':<24}"
    f"{'EXECUTED':<14}"
    f"{'FAILED':<12}"
    f"{'SKIPPED':<12}"
    f"{'STATUS':<18}"
)

print(subdivider)

scheduler_stats = {}

for row in rows:

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

    if scheduler not in scheduler_stats:

        scheduler_stats[
            scheduler
        ] = {
            "EXECUTED": 0,
            "FAILED": 0,
            "SKIPPED": 0
        }

    if result in scheduler_stats[scheduler]:

        scheduler_stats[
            scheduler
        ][
            result
        ] += 1

total_failures = 0

for scheduler, stats in scheduler_stats.items():

    executed = stats["EXECUTED"]
    failed = stats["FAILED"]
    skipped = stats["SKIPPED"]

    total_failures += failed

    if failed > 0:

        status = "UNSTABLE"

    elif executed > 0:

        status = "STABLE"

    else:

        status = "INACTIVE"

    print(
        f"{scheduler:<24}"
        f"{executed:<14}"
        f"{failed:<12}"
        f"{skipped:<12}"
        f"{status:<18}"
    )

print(subdivider)

print(
    f"{'TOTAL LOG EVENTS':<30}"
    f"{len(rows)}"
)

print(
    f"{'TOTAL FAILURES':<30}"
    f"{total_failures}"
)

print(subdivider)

#
# Runtime Assessment
#

if total_failures == 0:

    runtime_status = (
        "ORCHESTRATION STABLE"
    )

elif total_failures <= 3:

    runtime_status = (
        "MINOR FAILURE DETECTED"
    )

else:

    runtime_status = (
        "CRITICAL FAILURE STATE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END FAILURE INTELLIGENCE")
print(divider)
