from pathlib import Path
from datetime import datetime
import platform
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXPORT_DIR = (
    BASE_DIR /
    "exports"
)

EXPORT_DIR.mkdir(
    exist_ok=True
)

divider = "=" * 60

timestamp = (
    datetime.now().astimezone()
)

timestamp_slug = (
    timestamp.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )
)

export_file = (
    EXPORT_DIR /
    f"runtime_manifest_{timestamp_slug}.txt"
)

#
# Runtime Data
#

platform_name = "DIVAGG"

runtime_type = (
    "Terminal Runtime Platform"
)

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

#
# Runtime Counts
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
# Write Export
#

with open(export_file, "w") as file:

    file.write(
        f"{divider}\n"
    )

    file.write(
        "DIVAGG :: EXPORTED MANIFEST\n"
    )

    file.write(
        f"{divider}\n\n"
    )

    file.write(
        f"GENERATED :: "
        f"{timestamp}\n\n"
    )

    file.write(
        f"PLATFORM :: "
        f"{platform_name}\n"
    )

    file.write(
        f"RUNTIME TYPE :: "
        f"{runtime_type}\n"
    )

    file.write(
        f"LANGUAGE STACK :: "
        f"{language_stack}\n"
    )

    file.write(
        f"OPERATING SYSTEM :: "
        f"{operating_system}\n"
    )

    file.write(
        f"SYSTEM RELEASE :: "
        f"{system_release}\n"
    )

    file.write(
        f"PYTHON VERSION :: "
        f"{python_version}\n"
    )

    file.write(
        f"ARCHITECTURE :: "
        f"{architecture}\n"
    )

    file.write(
        f"CURRENT USER :: "
        f"{current_user}\n"
    )

    file.write(
        f"WORKING DIRECTORY :: "
        f"{working_directory}\n\n"
    )

    file.write(
        "RUNTIME TOPOLOGY\n"
    )

    file.write(
        f"{divider}\n"
    )

    file.write(
        f"PORTFOLIOS :: "
        f"{portfolio_count}\n"
    )

    file.write(
        f"SNAPSHOTS :: "
        f"{snapshot_count}\n"
    )

    file.write(
        f"BACKUPS :: "
        f"{backup_count}\n"
    )

    file.write(
        f"RUNTIME SNAPSHOTS :: "
        f"{runtime_snapshot_count}\n"
    )

    file.write(
        f"\n{divider}\n"
    )

#
# Output
#

print(divider)
print("DIVAGG :: EXPORT MANIFEST")
print(divider)

print("\n[SUCCESS] Runtime manifest exported:\n")

print(export_file)

print(f"\n{divider}")
print("END EXPORT MANIFEST")
print(divider)
