import tomllib
from pathlib import Path
import sys

CONFIG_FILE = Path("../config/config.toml")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: CONFIGURATION")
print(divider)

#
# Verify Config Exists
#

if not CONFIG_FILE.exists():

    print("\n[ERROR] Config file missing.")
    sys.exit(1)

#
# Load Config
#

try:

    with open(CONFIG_FILE, "rb") as file:

        config = tomllib.load(file)

except Exception as error:

    print(
        f"\n[ERROR] Failed loading config :: "
        f"{error}"
    )

    sys.exit(1)

#
# Output
#

print("\nACTIVE CONFIGURATION:\n")

print(subdivider)

for section, values in config.items():

    print(f"\n[{section}]")

    if isinstance(values, dict):

        for key, value in values.items():

            print(
                f"{key:<25}"
                f"{value}"
            )

    else:

        print(values)

print(f"\n{subdivider}")

print(divider)
print("END CONFIGURATION")
print(divider)
