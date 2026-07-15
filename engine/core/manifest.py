from pathlib import Path
from datetime import datetime
import platform
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: PLATFORM MANIFEST")
print(divider)

#
# Runtime Identity
#

platform_name = "DIVAGG"

runtime_type = "Terminal Runtime Platform"

language_stack = (
    "Python + Bash"
)

operating_system = (
    platform.system()
)

system_release = (
    platform.release()
)

python_version = (
    platform.python_version()
)

architecture = (
    platform.machine()
)

current_user = (
    os.getenv("USER")
)

working_directory = (
    BASE_DIR
)

timestamp = (
    datetime.now().astimezone()
)

#
# Filesystem Metrics
#

portfolio_count = len(
    list(
        (
            BASE_DIR /
            "data" /
            "portfolios"
        ).glob("*.csv")
    )
)

snapshot_count = len(
    list(
        (
            BASE_DIR /
            "snapshots"
        ).glob("*.csv")
    )
)

backup_count = len(
    list(
        (
            BASE_DIR /
            "backups"
        ).glob("*.tar.gz")
    )
)

runtime_snapshot_count = len(
    list(
        (
            BASE_DIR /
            "runtime_snapshots"
        ).glob("*.txt")
    )
)

#
# Output
#

print("\nPLATFORM IDENTITY:\n")

print(subdivider)

print(
    f"{'PLATFORM':<30}"
    f"{platform_name}"
)

print(
    f"{'RUNTIME TYPE':<30}"
    f"{runtime_type}"
)

print(
    f"{'LANGUAGE STACK':<30}"
    f"{language_stack}"
)

print(
    f"{'OPERATING SYSTEM':<30}"
    f"{operating_system}"
)

print(
    f"{'SYSTEM RELEASE':<30}"
    f"{system_release}"
)

print(
    f"{'PYTHON VERSION':<30}"
    f"{python_version}"
)

print(
    f"{'ARCHITECTURE':<30}"
    f"{architecture}"
)

print(
    f"{'CURRENT USER':<30}"
    f"{current_user}"
)

print(
    f"{'WORKING DIRECTORY':<30}"
    f"{working_directory}"
)

print(
    f"{'GENERATED':<30}"
    f"{timestamp}"
)

print(subdivider)

print("\nRUNTIME TOPOLOGY:\n")

print(subdivider)

print(
    f"{'PORTFOLIOS':<30}"
    f"{portfolio_count}"
)

print(
    f"{'SNAPSHOTS':<30}"
    f"{snapshot_count}"
)

print(
    f"{'BACKUPS':<30}"
    f"{backup_count}"
)

print(
    f"{'RUNTIME SNAPSHOTS':<30}"
    f"{runtime_snapshot_count}"
)

print(subdivider)

print(divider)
print("END PLATFORM MANIFEST")
print(divider)
