from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "logs"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: RUNTIME HEALTH")
print(divider)

checks = []

#
# Session Check
#

session_file = LOG_DIR / "session_start.txt"

checks.append(
    (
        "SESSION TRACKING",
        session_file.exists()
    )
)

#
# Command History Check
#

command_log = (
    LOG_DIR /
    "command_history.log"
)

checks.append(
    (
        "COMMAND HISTORY",
        command_log.exists()
    )
)

#
# Audit Log Check
#

audit_log = LOG_DIR / "audit.log"

checks.append(
    (
        "AUDIT LOG",
        audit_log.exists()
    )
)

#
# Backup Check
#

backup_count = len(
    list(
        (
            BASE_DIR /
            "backups"
        ).glob("*.tar.gz")
    )
)

checks.append(
    (
        "BACKUPS",
        backup_count > 0
    )
)

#
# Snapshot Check
#

snapshot_count = len(
    list(
        (
            BASE_DIR /
            "snapshots"
        ).glob("*.csv")
    )
)

checks.append(
    (
        "SNAPSHOTS",
        snapshot_count > 0
    )
)

#
# Runtime Snapshot Check
#

runtime_snapshot_count = len(
    list(
        (
            BASE_DIR /
            "runtime_snapshots"
        ).glob("*.txt")
    )
)

checks.append(
    (
        "RUNTIME SNAPSHOTS",
        runtime_snapshot_count > 0
    )
)

#
# Storage Check
#

total_storage = 0

for item in BASE_DIR.rglob("*"):

    if item.is_file():

        total_storage += (
            item.stat().st_size
        )

storage_kb = total_storage / 1024

checks.append(
    (
        "STORAGE FOOTPRINT",
        storage_kb < 50000
    )
)

#
# Scoring
#

passed = sum(
    1 for _, result in checks
    if result
)

total = len(checks)

health_score = int(
    (passed / total) * 100
)

#
# Status
#

if health_score >= 90:

    status = "OPTIMAL"

elif health_score >= 70:

    status = "STABLE"

else:

    status = "ATTENTION"

#
# Output
#

print("\nRUNTIME STATUS:\n")

print(subdivider)

for name, result in checks:

    state = (
        "OK"
        if result
        else "MISSING"
    )

    print(
        f"{name:<30}"
        f"{state}"
    )

print(subdivider)

print(
    f"{'HEALTH SCORE':<30}"
    f"{health_score}/100"
)

print(
    f"{'STATUS':<30}"
    f"{status}"
)

print(
    f"{'TOTAL STORAGE':<30}"
    f"{storage_kb:.2f} KB"
)

print(subdivider)

print(divider)
print("END RUNTIME HEALTH")
print(divider)
