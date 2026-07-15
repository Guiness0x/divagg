import os
import platform
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: ENVIRONMENT")
print(divider)

#
# Environment Data
#

python_version = platform.python_version()

system_name = platform.system()
system_release = platform.release()

machine_arch = platform.machine()

current_user = os.getenv("USER")

working_directory = BASE_DIR

#
# Output
#

print("\nRUNTIME ENVIRONMENT:\n")

print(subdivider)

print(
    f"{'PYTHON VERSION':<30}"
    f"{python_version}"
)

print(
    f"{'OPERATING SYSTEM':<30}"
    f"{system_name}"
)

print(
    f"{'SYSTEM RELEASE':<30}"
    f"{system_release}"
)

print(
    f"{'ARCHITECTURE':<30}"
    f"{machine_arch}"
)

print(
    f"{'CURRENT USER':<30}"
    f"{current_user}"
)

print(
    f"{'WORKING DIRECTORY':<30}"
    f"{working_directory}"
)

print(subdivider)

print(divider)
print("END ENVIRONMENT")
print(divider)
