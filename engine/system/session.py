from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SESSION_FILE = (
    BASE_DIR /
    "logs" /
    "session_start.txt"
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SESSION")
print(divider)

if not SESSION_FILE.exists():

    print("\n[ERROR] Session file missing.")
    raise SystemExit(1)

with open(SESSION_FILE) as file:

    session_timestamp = file.read().strip()

session_start = datetime.fromisoformat(
    session_timestamp
)

current_time = datetime.now(
    session_start.tzinfo
)

uptime = current_time - session_start

print("\nSESSION INFORMATION:\n")

print(subdivider)

print(
    f"{'SESSION START':<25}"
    f"{session_start}"
)

print(
    f"{'CURRENT TIME':<25}"
    f"{current_time}"
)

print(
    f"{'SESSION UPTIME':<25}"
    f"{uptime}"
)

print(subdivider)

print(divider)
print("END SESSION")
print(divider)
