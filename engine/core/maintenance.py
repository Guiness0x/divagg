from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "logs"
BACKUP_DIR = BASE_DIR / "backups"
SNAPSHOT_DIR = BASE_DIR / "snapshots"

SESSION_FILE = LOG_DIR / "session_start.txt"
COMMAND_LOG = LOG_DIR / "command_history.log"
AUDIT_LOG = LOG_DIR / "audit.log"

STORAGE_TARGETS = [
    BASE_DIR / "data",
    BASE_DIR / "exports",
    BASE_DIR / "reports",
    BASE_DIR / "snapshots",
    BASE_DIR / "logs",
    BASE_DIR / "simulations",
    BASE_DIR / "backups",
    BASE_DIR / "config"
]

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: MAINTENANCE OVERVIEW")
print(divider)

def count_lines(path):

    if not path.exists():
        return 0

    with open(path) as file:
        return len(file.readlines())

def count_files(path, pattern="*"):

    if not path.exists():
        return 0

    return len(list(path.glob(pattern)))

def calculate_size(path):

    total = 0

    if not path.exists():
        return 0

    if path.is_file():
        return path.stat().st_size

    for item in path.rglob("*"):

        if item.is_file():
            total += item.stat().st_size

    return total

session_uptime = "UNKNOWN"

if SESSION_FILE.exists():

    with open(SESSION_FILE) as file:

        session_timestamp = file.read().strip()

    try:

        session_start = datetime.fromisoformat(
            session_timestamp
        )

        current_time = datetime.now(
            session_start.tzinfo
        )

        session_uptime = str(
            current_time - session_start
        )

    except Exception:

        session_uptime = "INVALID SESSION TIME"

command_count = count_lines(COMMAND_LOG)
audit_count = count_lines(AUDIT_LOG)

backup_count = count_files(
    BACKUP_DIR,
    "*.tar.gz"
)

snapshot_count = count_files(
    SNAPSHOT_DIR,
    "*.csv"
)

total_storage = 0

for target in STORAGE_TARGETS:

    total_storage += calculate_size(target)

total_storage_kb = total_storage / 1024

print("\nMAINTENANCE STATUS:\n")
print(subdivider)

print(
    f"{'SESSION UPTIME':<30}"
    f"{session_uptime}"
)

print(
    f"{'COMMAND EVENTS':<30}"
    f"{command_count}"
)

print(
    f"{'AUDIT EVENTS':<30}"
    f"{audit_count}"
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
    f"{'TOTAL STORAGE':<30}"
    f"{total_storage_kb:.2f} KB"
)

print(subdivider)

print("\nRECOMMENDED CHECKS:\n")
print(subdivider)

print("./divagg integrity")
print("./divagg backup")
print("./divagg storage")
print("./divagg logs")

print(subdivider)
print(divider)
print("END MAINTENANCE")
print(divider)
