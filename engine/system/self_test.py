from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SELF TEST")
print(divider)

checks = []

#
# Core Runtime Files
#

runtime_files = [

    BASE_DIR / "divagg",

    BASE_DIR / "engine" / "manifest.py",
    BASE_DIR / "engine" / "version.py",
    BASE_DIR / "engine" / "runtime_health.py",
    BASE_DIR / "engine" / "readiness.py",
    BASE_DIR / "engine" / "backup.py",
    BASE_DIR / "engine" / "integrity.py",
]

for file in runtime_files:

    checks.append(
        (
            f"FILE {file.name}",
            file.exists()
        )
    )

#
# Critical Directories
#

runtime_directories = [

    BASE_DIR / "engine",
    BASE_DIR / "logs",
    BASE_DIR / "exports",
    BASE_DIR / "reports",
    BASE_DIR / "snapshots",
    BASE_DIR / "backups",
    BASE_DIR / "runtime_snapshots"
]

for directory in runtime_directories:

    checks.append(
        (
            f"DIR {directory.name}",
            directory.exists()
        )
    )

#
# Runtime Logs
#

runtime_logs = [

    BASE_DIR / "logs" / "command_history.log",
    BASE_DIR / "logs" / "session_start.txt"
]

for log in runtime_logs:

    checks.append(
        (
            f"LOG {log.name}",
            log.exists()
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

if score >= 95:

    status = "CORE STABLE"

elif score >= 80:

    status = "STABLE"

else:

    status = "ATTENTION"

#
# Output
#

print("\nSELF TEST RESULTS:\n")

print(subdivider)

for name, result in checks:

    state = (
        "PASS"
        if result
        else "FAIL"
    )

    print(
        f"{name:<40}"
        f"{state}"
    )

print(subdivider)

print(
    f"{'SELF TEST SCORE':<40}"
    f"{score}/100"
)

print(
    f"{'STATUS':<40}"
    f"{status}"
)

print(subdivider)

print(divider)
print("END SELF TEST")
print(divider)
