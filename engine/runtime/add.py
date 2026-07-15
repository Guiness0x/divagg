import csv
from pathlib import Path
from datetime import datetime
import shutil
import sys

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

from utils.registry import (
    load_registry_tickers
)

from utils.audit import (
    write_audit_log
)

SNAPSHOT_DIR = Path("../snapshots")

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

divider = "=" * 60

print(divider)
print("DIVAGG :: ADD POSITION")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

if not PORTFOLIO_FILE.exists():

    print("\n[ERROR] Portfolio not found.")
    print(PORTFOLIO_FILE)

    sys.exit(1)

#
# Load Registry
#

try:

    valid_tickers = load_registry_tickers()

except Exception as error:

    print(f"\n[ERROR] Failed loading registry :: {error}")
    sys.exit(1)

#
# Automatic Snapshot
#

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

snapshot_path = (
    SNAPSHOT_DIR /
    f"{ACTIVE_PORTFOLIO}_snapshot_{timestamp}.csv"
)

shutil.copy2(PORTFOLIO_FILE, snapshot_path)

print("\n[INFO] Automatic snapshot created:")
print(snapshot_path)

#
# User Input
#

print("\nENTER POSITION DATA\n")

ticker = input(
    "Ticker      : "
).strip().upper()

if ticker not in valid_tickers:

    print("\n[ERROR] Unknown ticker.")
    print("Ticker does not exist in registry.")

    sys.exit(1)

shares_input = input(
    "Shares      : "
).strip()

dividend_input = input(
    "Dividend    : "
).strip()

frequency = input(
    "Frequency   : "
).strip().lower()

#
# Validation
#

try:

    shares = float(shares_input)

    if shares < 0:
        raise ValueError

except Exception:

    print("\n[ERROR] Invalid shares value.")
    sys.exit(1)

try:

    dividend = float(dividend_input)

    if dividend < 0:
        raise ValueError

except Exception:

    print("\n[ERROR] Invalid dividend value.")
    sys.exit(1)

if frequency not in VALID_FREQUENCIES:

    print("\n[ERROR] Invalid frequency.")
    print(
        "Valid options: "
        "monthly, quarterly, yearly"
    )

    sys.exit(1)

#
# Safe Append
#

try:

    with open(PORTFOLIO_FILE, "a", newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            ticker,
            shares,
            dividend,
            frequency
        ])

    #
    # Audit Logging
    #

    write_audit_log(
        "ADD",
        (
            f"portfolio={ACTIVE_PORTFOLIO} | "
            f"ticker={ticker} | "
            f"shares={shares} | "
            f"dividend={dividend} | "
            f"frequency={frequency}"
        )
    )

    print("\n[SUCCESS] Position added:")

    print(
        f"{ticker} | "
        f"{shares} shares | "
        f"{dividend} dividend | "
        f"{frequency}"
    )

except Exception as error:

    print(
        f"\n[ERROR] Failed to append row :: "
        f"{error}"
    )

    sys.exit(1)

print(f"\n{divider}")
print("END ADD POSITION")
print(divider)
