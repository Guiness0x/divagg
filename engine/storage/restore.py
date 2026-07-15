from pathlib import Path
import shutil
import sys

SNAPSHOT_DIR = Path("../snapshots")
PORTFOLIO_FILE = Path("../data/portfolio.csv")

divider = "=" * 60

print(divider)
print("DIVAGG :: RESTORE SNAPSHOT")
print(divider)

snapshots = sorted(
    SNAPSHOT_DIR.glob("*.csv"),
    key=lambda f: f.stat().st_mtime,
    reverse=True
)

if not snapshots:

    print("\n[ERROR] No snapshots found.")
    sys.exit(1)

print("\nAVAILABLE SNAPSHOTS:\n")

for index, snapshot in enumerate(snapshots, start=1):

    print(f"{index}. {snapshot.name}")

selection = input(
    "\nSelect snapshot number : "
).strip()

try:

    selection_index = int(selection) - 1

    if (
        selection_index < 0 or
        selection_index >= len(snapshots)
    ):
        raise ValueError

except Exception:

    print("\n[ERROR] Invalid selection.")
    sys.exit(1)

selected_snapshot = snapshots[selection_index]

print("\nSELECTED SNAPSHOT:\n")
print(selected_snapshot.name)

confirmation = input(
    "\nConfirm restore? (yes/no) : "
).strip().lower()

if confirmation != "yes":

    print("\n[INFO] Restore cancelled.")
    sys.exit(0)

try:

    shutil.copy2(
        selected_snapshot,
        PORTFOLIO_FILE
    )

    print("\n[SUCCESS] Portfolio restored.")
    print(f"Source: {selected_snapshot.name}")

except Exception as error:

    print(f"\n[ERROR] Restore failed :: {error}")
    sys.exit(1)

print(f"\n{divider}")
print("END RESTORE")
print(divider)
