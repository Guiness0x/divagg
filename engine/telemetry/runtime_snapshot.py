from pathlib import Path
from datetime import datetime
import platform
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "logs"
SNAPSHOT_DIR = BASE_DIR / "runtime_snapshots"

SNAPSHOT_DIR.mkdir(
    exist_ok=True
)

SESSION_FILE = LOG_DIR / "session_start.txt"
COMMAND_LOG = LOG_DIR / "command_history.log"

divider = "=" * 60

def calculate_size(path):

    total = 0

    if not path.exists():
        return 0

    for item in path.rglob("*"):

        if item.is_file():

            total += item.stat().st_size

    return total

#
# Runtime Data
#

current_time = datetime.now().astimezone()

python_version = platform.python_version()

system_name = platform.system()

system_release = platform.release()

architecture = platform.machine()

current_user = os.getenv("USER")

session_uptime = "UNKNOWN"

if SESSION_FILE.exists():

    with open(SESSION_FILE) as file:

        session_timestamp = file.read().strip()

    try:

        session_start = datetime.fromisoformat(
            session_timestamp
        )

        session_uptime = str(
            current_time - session_start
        )

    except Exception:

        session_uptime = "INVALID"

command_count = 0

if COMMAND_LOG.exists():

    with open(COMMAND_LOG) as file:

        command_count = len(
            file.readlines()
        )

total_storage = calculate_size(
    BASE_DIR
) / 1024

#
# Snapshot File
#

timestamp = current_time.strftime(
    "%Y-%m-%d_%H-%M-%S"
)

snapshot_file = (
    SNAPSHOT_DIR /
    f"runtime_snapshot_{timestamp}.txt"
)

with open(snapshot_file, "w") as file:

    file.write(
        f"{divider}\n"
    )

    file.write(
        "DIVAGG :: RUNTIME SNAPSHOT\n"
    )

    file.write(
        f"{divider}\n\n"
    )

    file.write(
        f"SNAPSHOT TIME :: "
        f"{current_time}\n"
    )

    file.write(
        f"PYTHON VERSION :: "
        f"{python_version}\n"
    )

    file.write(
        f"OPERATING SYSTEM :: "
        f"{system_name}\n"
    )

    file.write(
        f"SYSTEM RELEASE :: "
        f"{system_release}\n"
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
        f"SESSION UPTIME :: "
        f"{session_uptime}\n"
    )

    file.write(
        f"COMMAND EVENTS :: "
        f"{command_count}\n"
    )

    file.write(
        f"TOTAL STORAGE :: "
        f"{total_storage:.2f} KB\n"
    )

    file.write(
        f"\n{divider}\n"
    )

print(divider)
print("DIVAGG :: RUNTIME SNAPSHOT")
print(divider)

print("\n[SUCCESS] Runtime snapshot created:\n")

print(snapshot_file)

print(f"\n{divider}")
print("END RUNTIME SNAPSHOT")
print(divider)
