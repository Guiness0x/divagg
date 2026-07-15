from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CACHE_DIR = (
    BASE_DIR /
    "data" /
    "feeds" /
    "cache"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: FEED CACHE")
print(divider)

CACHE_DIR.mkdir(
    exist_ok=True
)

cache_files = sorted(
    CACHE_DIR.glob("*")
)

valid_files = [
    file for file in cache_files
    if file.is_file()
]

print("\nFEED CACHE STATUS:\n")

print(subdivider)

print(
    f"{'CACHE DIRECTORY':<30}"
    f"{CACHE_DIR}"
)

print(
    f"{'CACHE FILES':<30}"
    f"{len(valid_files)}"
)

print(subdivider)

if valid_files:

    print("\nCACHE INVENTORY:\n")
    print(subdivider)

    for file in valid_files:

        print(
            f"{file.name:<40}"
            f"{file.stat().st_size} bytes"
        )

    print(subdivider)

else:

    print("\n[INFO] No cached feed files found.\n")

print(divider)
print("END FEED CACHE")
print(divider)
