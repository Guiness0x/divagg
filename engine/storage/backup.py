from pathlib import Path
from datetime import datetime
import tarfile
import sys

BACKUP_DIR = Path("../backups")

TARGETS = [
    "../data",
    "../exports",
    "../reports",
    "../snapshots",
    "../logs",
    "../simulations",
    "../config"
]

divider = "=" * 60

print(divider)
print("DIVAGG :: FULL SYSTEM BACKUP")
print(divider)

#
# Prepare Backup Directory
#

BACKUP_DIR.mkdir(
    parents=True,
    exist_ok=True
)

timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)

backup_file = (
    BACKUP_DIR /
    f"divagg_backup_{timestamp}.tar.gz"
)

#
# Create Archive
#

try:

    with tarfile.open(
        backup_file,
        "w:gz"
    ) as archive:

        for target in TARGETS:

            path = Path(target)

            if path.exists():

                archive.add(
                    path,
                    arcname=path.name
                )

except Exception as error:

    print(
        f"\n[ERROR] Backup failed :: "
        f"{error}"
    )

    sys.exit(1)

#
# Output
#

print("\n[SUCCESS] Backup archive created:\n")

print(backup_file)

print(f"\n{divider}")
print("END BACKUP")
print(divider)
