from pathlib import Path
import sys

AUDIT_LOG = Path("../logs/audit.log")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: AUDIT LOG")
print(divider)

#
# Verify Log Exists
#

if not AUDIT_LOG.exists():

    print("\n[INFO] No audit log found.")
    sys.exit(0)

#
# Load Entries
#

try:

    with open(AUDIT_LOG, "r") as logfile:

        entries = logfile.readlines()

except Exception as error:

    print(
        f"\n[ERROR] Failed reading audit log :: "
        f"{error}"
    )

    sys.exit(1)

if not entries:

    print("\n[INFO] Audit log is empty.")
    sys.exit(0)

#
# Output
#

print("\nRECENT EVENTS:\n")

print(subdivider)

for entry in reversed(entries[-20:]):

    print(entry.strip())

print(subdivider)

print(
    f"TOTAL EVENTS : "
    f"{len(entries)}"
)

print(divider)
print("END AUDIT LOG")
print(divider)
