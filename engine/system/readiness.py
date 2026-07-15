from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: RUNTIME READINESS")
print(divider)

checks = []

#
# Core Directories
#

required_directories = [

    BASE_DIR / "engine",
    BASE_DIR / "logs",
    BASE_DIR / "data",
    BASE_DIR / "exports",
    BASE_DIR / "reports",
    BASE_DIR / "snapshots",
    BASE_DIR / "backups",
    BASE_DIR / "runtime_snapshots"
]

for directory in required_directories:

    checks.append(
        (
            f"DIR {directory.name}",
            directory.exists()
        )
    )

#
# Runtime Files
#

runtime_files = [

    BASE_DIR / "logs" / "command_history.log",
    BASE_DIR / "logs" / "session_start.txt",
    BASE_DIR / "logs" / "audit.log"
]

for runtime_file in runtime_files:

    checks.append(
        (
            f"FILE {runtime_file.name}",
            runtime_file.exists()
        )
    )

#
# Snapshot Presence
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
        "PORTFOLIO SNAPSHOTS",
        snapshot_count > 0
    )
)

#
# Backup Presence
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
        "BACKUP ARCHIVES",
        backup_count > 0
    )
)

#
# Runtime Snapshot Presence
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
# Score
#

passed = sum(
    1 for _, result in checks
    if result
)

total = len(checks)

score = int(
    (passed / total) * 100
)

#
# Status
#

if score >= 90:

    status = "DEPLOYMENT READY"

elif score >= 70:

    status = "MOSTLY READY"

else:

    status = "NOT READY"

#
# Output
#

print("\nREADINESS CHECKS:\n")

print(subdivider)

for name, result in checks:

    state = (
        "OK"
        if result
        else "MISSING"
    )

    print(
        f"{name:<35}"
        f"{state}"
    )

print(subdivider)

print(
    f"{'READINESS SCORE':<35}"
    f"{score}/100"
)

print(
    f"{'STATUS':<35}"
    f"{status}"
)

print(subdivider)

print(divider)
print("END RUNTIME READINESS")
print(divider)
