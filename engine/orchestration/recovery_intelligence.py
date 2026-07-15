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
print("DIVAGG :: RECOVERY INTELLIGENCE")
print(divider)

if not SCHEDULER_LOG.exists():
    print("\n[ERROR] Scheduler runtime log missing.")
    raise SystemExit(1)

with open(
    SCHEDULER_LOG,
    newline="",
    encoding="utf-8"
) as csvfile:
    rows = list(csv.DictReader(csvfile))

scheduler_stats = {}

for row in rows:
    scheduler = row.get("scheduler") or "UNKNOWN"
    result = row.get("result") or "UNKNOWN"

    if scheduler not in scheduler_stats:
        scheduler_stats[scheduler] = {
            "EXECUTED": 0,
            "FAILED": 0,
            "SKIPPED": 0
        }

    if result in scheduler_stats[scheduler]:
        scheduler_stats[scheduler][result] += 1

print("\nRECOVERY GUIDANCE:\n")
print(subdivider)

print(
    f"{'SCHEDULER':<24}"
    f"{'STATE':<18}"
    f"{'RECOVERY ACTION':<40}"
)

print(subdivider)

recovery_actions = 0

for scheduler, stats in scheduler_stats.items():
    executed = stats["EXECUTED"]
    failed = stats["FAILED"]
    skipped = stats["SKIPPED"]

    if failed > 0:
        state = "FAILED"
        action = "inspect command, rerun scheduler"
        recovery_actions += 1

    elif executed > 0:
        state = "STABLE"
        action = "no action required"

    elif skipped > 0:
        state = "INACTIVE"
        action = "attach command when provider is ready"
        recovery_actions += 1

    else:
        state = "UNKNOWN"
        action = "inspect scheduler registry"
        recovery_actions += 1

    print(
        f"{scheduler:<24}"
        f"{state:<18}"
        f"{action:<40}"
    )

print(subdivider)

print(
    f"{'RECOVERY ACTIONS':<30}"
    f"{recovery_actions}"
)

if recovery_actions == 0:
    runtime_status = "NO RECOVERY REQUIRED"
elif recovery_actions <= 2:
    runtime_status = "MINOR RECOVERY GUIDANCE"
else:
    runtime_status = "RECOVERY ATTENTION REQUIRED"

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END RECOVERY INTELLIGENCE")
print(divider)
