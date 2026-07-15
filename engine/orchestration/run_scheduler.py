import csv
import subprocess

from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SCHEDULER_REGISTRY = (
    BASE_DIR /
    "data" /
    "schedulers" /
    "scheduler_registry.csv"
)

SCHEDULER_LOG = (
    BASE_DIR /
    "logs" /
    "schedulers" /
    "scheduler_runtime_log.csv"
)

DIVAGG = (
    BASE_DIR /
    "divagg"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: RUN SCHEDULER")
print(divider)

if not SCHEDULER_REGISTRY.exists():

    print("\n[ERROR] Scheduler registry missing.")
    raise SystemExit(1)

if not DIVAGG.exists():

    print("\n[ERROR] DIVAGG router missing.")
    raise SystemExit(1)

#
# Ensure Scheduler Log Exists
#

if not SCHEDULER_LOG.exists():

    with open(
        SCHEDULER_LOG,
        "w",
        newline="",
        encoding="utf-8"
    ) as logfile:

        writer = csv.writer(
            logfile
        )

        writer.writerow([
            "timestamp",
            "scheduler",
            "command",
            "result"
        ])

#
# Load Scheduler Registry
#

with open(
    SCHEDULER_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

job_map = {
    "spreadsheet_sync": "sync-spreadsheet",
    "runtime_enrichment": "enrich-registry"
}

print("\nSCHEDULER EXECUTION:\n")

print(subdivider)

print(
    f"{'SCHEDULER':<24}"
    f"{'COMMAND':<22}"
    f"{'RESULT':<18}"
)

print(subdivider)

executed_jobs = 0
skipped_jobs = 0
failed_jobs = 0

execution_timestamp = (
    datetime.now(
        timezone.utc
    ).isoformat()
)

for row in rows:

    scheduler_name = (
        row.get("scheduler_name")
        or "UNKNOWN"
    )

    status = (
        row.get("status")
        or "UNKNOWN"
    )

    command = job_map.get(
        scheduler_name
    )

    if status != "active" or not command:

        skipped_jobs += 1

        result_state = "SKIPPED"

        print(
            f"{scheduler_name:<24}"
            f"{str(command or 'none'):<22}"
            f"{result_state:<18}"
        )

    else:

        result = subprocess.run(
            [
                str(DIVAGG),
                command
            ],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            executed_jobs += 1
            result_state = "EXECUTED"

        else:

            failed_jobs += 1
            result_state = "FAILED"

        print(
            f"{scheduler_name:<24}"
            f"{command:<22}"
            f"{result_state:<18}"
        )

    #
    # Persist Runtime Log
    #

    with open(
        SCHEDULER_LOG,
        "a",
        newline="",
        encoding="utf-8"
    ) as logfile:

        writer = csv.writer(
            logfile
        )

        writer.writerow([
            execution_timestamp,
            scheduler_name,
            command or "none",
            result_state
        ])

print(subdivider)

print(
    f"{'EXECUTED JOBS':<30}"
    f"{executed_jobs}"
)

print(
    f"{'SKIPPED JOBS':<30}"
    f"{skipped_jobs}"
)

print(
    f"{'FAILED JOBS':<30}"
    f"{failed_jobs}"
)

print(
    f"{'RUN TIMESTAMP':<30}"
    f"{execution_timestamp}"
)

print(subdivider)

if failed_jobs > 0:

    runtime_status = (
        "SCHEDULER ERRORS"
    )

elif executed_jobs == 0:

    runtime_status = (
        "NO JOBS EXECUTED"
    )

else:

    runtime_status = (
        "SCHEDULER EXECUTION STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END RUN SCHEDULER")
print(divider)
