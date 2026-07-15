from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOG_DIR = BASE_DIR / "logs"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: LOG INSPECTION")
print(divider)

#
# Verify Log Directory
#

if not LOG_DIR.exists():

    print("\n[ERROR] Log directory missing.")
    raise SystemExit(1)

#
# Gather Logs
#

log_files = sorted(
    LOG_DIR.glob("*.log")
)

print("\nAVAILABLE LOGS:\n")

print(subdivider)

if not log_files:

    print("No log files found.")

else:

    for log_file in log_files:

        size = log_file.stat().st_size

        print(
            f"{log_file.name:<35}"
            f"{size} bytes"
        )

print(subdivider)

#
# Latest Log
#

if log_files:

    latest_log = log_files[-1]

    print("\nLATEST LOG:\n")

    print(subdivider)

    print(latest_log.name)

    print(subdivider)

print(divider)
print("END LOG INSPECTION")
print(divider)
