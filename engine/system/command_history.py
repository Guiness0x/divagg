from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

COMMAND_LOG = (
    BASE_DIR /
    "logs" /
    "command_history.log"
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: COMMAND HISTORY")
print(divider)

#
# Verify Log
#

if not COMMAND_LOG.exists():

    print("\n[INFO] No command history found.")
    raise SystemExit(0)

#
# Read Entries
#

with open(COMMAND_LOG) as logfile:

    entries = [
        line.strip()
        for line in logfile
        if line.strip()
    ]

print("\nRECENT COMMANDS:\n")

print(subdivider)

if not entries:

    print("No command entries found.")

else:

    recent_entries = entries[-15:]

    for entry in recent_entries:

        print(entry)

print(subdivider)

print(
    f"TOTAL COMMANDS : "
    f"{len(entries)}"
)

print(divider)
print("END COMMAND HISTORY")
print(divider)
