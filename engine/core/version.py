from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VERSION = "0.1.0"
BUILD_STAGE = "Main Engine Runtime"
BUILD_STATUS = "Active Development"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: VERSION")
print(divider)

print("\nRUNTIME VERSION:\n")

print(subdivider)

print(
    f"{'VERSION':<25}"
    f"{VERSION}"
)

print(
    f"{'BUILD STAGE':<25}"
    f"{BUILD_STAGE}"
)

print(
    f"{'BUILD STATUS':<25}"
    f"{BUILD_STATUS}"
)

print(
    f"{'ROOT DIRECTORY':<25}"
    f"{BASE_DIR}"
)

print(
    f"{'CHECKED AT':<25}"
    f"{datetime.now().astimezone()}"
)

print(subdivider)

print(divider)
print("END VERSION")
print(divider)
