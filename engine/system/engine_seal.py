from pathlib import Path
from datetime import datetime
import tarfile

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SEAL_DIR = (
    BASE_DIR /
    "engine_seals"
)

SEAL_DIR.mkdir(
    exist_ok=True
)

divider = "=" * 60

print(divider)
print("DIVAGG :: ENGINE SEAL")
print(divider)

#
# Seal Timestamp
#

timestamp = (
    datetime.now().astimezone()
)

timestamp_slug = (
    timestamp.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )
)

#
# Seal Manifest
#

seal_manifest = (
    SEAL_DIR /
    f"core_engine_seal_{timestamp_slug}.txt"
)

with open(seal_manifest, "w") as file:

    file.write(
        f"{divider}\n"
    )

    file.write(
        "DIVAGG :: CORE ENGINE SEAL\n"
    )

    file.write(
        f"{divider}\n\n"
    )

    file.write(
        f"SEALED AT :: "
        f"{timestamp}\n\n"
    )

    file.write(
        "CORE ENGINE GENERATION :: 0.1\n"
    )

    file.write(
        "STATUS :: CORE STABLE\n"
    )

    file.write(
        "RUNTIME TYPE :: "
        "Terminal Runtime Platform\n"
    )

    file.write(
        "LANGUAGE STACK :: "
        "Python + Bash\n"
    )

    file.write(
        "\nFOUNDATIONAL SYSTEMS\n"
    )

    file.write(
        f"{divider}\n"
    )

    systems = [

        "Runtime Identity",
        "Runtime Lifecycle",
        "Runtime Diagnostics",
        "Runtime Verification",
        "Operational Infrastructure",
        "Protection Infrastructure",
        "Historical Infrastructure"
    ]

    for system in systems:

        file.write(
            f"- {system}\n"
        )

    file.write(
        f"\n{divider}\n"
    )

#
# Seal Archive
#

archive_path = (
    SEAL_DIR /
    f"core_engine_archive_{timestamp_slug}.tar.gz"
)

with tarfile.open(
    archive_path,
    "w:gz"
) as archive:

    archive.add(
        BASE_DIR,
        arcname="divagg"
    )

#
# Output
#

print("\n[CORE ENGINE SEALED]\n")

print(
    f"SEAL MANIFEST ::\n"
    f"{seal_manifest}\n"
)

print(
    f"SEAL ARCHIVE ::\n"
    f"{archive_path}"
)

print(f"\n{divider}")
print("END ENGINE SEAL")
print(divider)
