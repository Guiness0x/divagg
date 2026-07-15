from pathlib import Path
import csv
import sys

PORTFOLIO_DIR = Path("../data/portfolios")
SNAPSHOT_DIR = Path("../snapshots")
REGISTRY_FILE = Path("../data/registry/tickers.csv")
AUDIT_LOG = Path("../logs/audit.log")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SYSTEM METRICS")
print(divider)

#
# Portfolio Count
#

try:

    portfolios = list(
        PORTFOLIO_DIR.glob("*.csv")
    )

    portfolio_count = len(portfolios)

except Exception:

    portfolio_count = 0

#
# Snapshot Count
#

try:

    snapshots = list(
        SNAPSHOT_DIR.glob("*.csv")
    )

    snapshot_count = len(snapshots)

except Exception:

    snapshot_count = 0

#
# Registry Count
#

registry_count = 0

try:

    with open(REGISTRY_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for _ in reader:

            registry_count += 1

except Exception:

    registry_count = 0

#
# Audit Event Count
#

audit_count = 0

try:

    if AUDIT_LOG.exists():

        with open(AUDIT_LOG, "r") as logfile:

            audit_count = len(
                logfile.readlines()
            )

except Exception:

    audit_count = 0

#
# Output
#

print("\nSYSTEM OVERVIEW:\n")

print(subdivider)

print(
    f"{'PORTFOLIOS':<30}"
    f"{portfolio_count}"
)

print(
    f"{'SNAPSHOTS':<30}"
    f"{snapshot_count}"
)

print(
    f"{'REGISTRY ENTRIES':<30}"
    f"{registry_count}"
)

print(
    f"{'AUDIT EVENTS':<30}"
    f"{audit_count}"
)

print(subdivider)

print(divider)
print("END METRICS")
print(divider)
