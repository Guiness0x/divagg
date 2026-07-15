from pathlib import Path
import sys

from utils.loader import (
    ACTIVE_PORTFOLIO
)

SNAPSHOT_DIR = Path("../snapshots")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SNAPSHOT HISTORY")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

#
# Locate Snapshots
#

try:

    snapshots = sorted(
        SNAPSHOT_DIR.glob(
            f"{ACTIVE_PORTFOLIO}_snapshot_*.csv"
        ),
        reverse=True
    )

except Exception as error:

    print(f"\n[ERROR] Snapshot scan failed :: {error}")
    sys.exit(1)

if not snapshots:

    print("\n[INFO] No snapshots found.")
    sys.exit(0)

#
# Output
#

print("\nSNAPSHOT TIMELINE:\n")

print(subdivider)

for index, snapshot in enumerate(snapshots, start=1):

    print(
        f"{index}. "
        f"{snapshot.name}"
    )

print(subdivider)

print(
    f"TOTAL SNAPSHOTS : "
    f"{len(snapshots)}"
)

print(divider)
print("END SNAPSHOT HISTORY")
print(divider)
