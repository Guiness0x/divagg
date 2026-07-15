from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SESSION_FILE = (
    BASE_DIR /
    "logs" /
    "session_start.txt"
)

divider = "=" * 60

print(divider)
print("DIVAGG :: RESET SESSION")
print(divider)

#
# Reset Session Timestamp
#

new_timestamp = datetime.now().astimezone()

with open(SESSION_FILE, "w") as file:

    file.write(
        new_timestamp.isoformat()
    )

#
# Output
#

print("\n[SUCCESS] Runtime session reset.\n")

print(
    f"NEW SESSION START :: "
    f"{new_timestamp}"
)

print(f"\n{divider}")
print("END RESET SESSION")
print(divider)
