import csv
import sys
import tomllib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.toml"
PORTFOLIO_DIR = BASE_DIR / "data" / "portfolios"
REGISTRY_FILE = BASE_DIR / "data" / "registry" / "tickers.csv"

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

PORTFOLIO_HEADERS = [
    "ticker",
    "shares",
    "dividend",
    "frequency"
]

REGISTRY_HEADERS = [
    "ticker",
    "name",
    "sector",
    "asset_type",
    "payout_frequency"
]

issues = []

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: PLATFORM INTEGRITY CHECK")
print(divider)

#
# CONFIG CHECK
#

print("\nCONFIG CHECK:\n")
print(subdivider)

if not CONFIG_FILE.exists():

    print("config.toml              MISSING")
    issues.append("Missing config.toml")

else:

    try:

        with open(CONFIG_FILE, "rb") as config_file:

            tomllib.load(config_file)

        print("config.toml              OK")

    except Exception as error:

        print(f"config.toml              ERROR :: {error}")
        issues.append(str(error))

print(subdivider)

#
# REGISTRY CHECK
#

print("\nREGISTRY CHECK:\n")
print(subdivider)

registry_tickers = set()

if not REGISTRY_FILE.exists():

    print("tickers.csv              MISSING")
    issues.append("Missing registry")

else:

    try:

        with open(REGISTRY_FILE, newline="") as csvfile:

            reader = csv.DictReader(csvfile)

            if reader.fieldnames != REGISTRY_HEADERS:

                print("registry headers         INVALID")
                issues.append("Invalid registry headers")

            else:

                print("registry headers         OK")

            for row in reader:

                registry_tickers.add(
                    row["ticker"].upper()
                )

    except Exception as error:

        print(f"registry                 ERROR :: {error}")
        issues.append(str(error))

print(subdivider)

#
# PORTFOLIO CHECKS
#

print("\nPORTFOLIO CHECKS:\n")
print(subdivider)

portfolio_files = sorted(
    PORTFOLIO_DIR.glob("*.csv")
)

for portfolio_file in portfolio_files:

    try:

        with open(portfolio_file, newline="") as csvfile:

            reader = csv.DictReader(csvfile)

            if reader.fieldnames != PORTFOLIO_HEADERS:

                print(f"{portfolio_file.name:<25} INVALID")

                issues.append(
                    f"Invalid headers :: "
                    f"{portfolio_file.name}"
                )

                continue

            row_count = 0

            for line_number, row in enumerate(reader, start=2):

                row_count += 1

                ticker = row["ticker"].upper()
                frequency = row["frequency"].lower()

                try:

                    shares = float(row["shares"])
                    dividend = float(row["dividend"])

                except Exception:

                    issues.append(
                        f"Invalid numeric value :: "
                        f"{portfolio_file.name}:{line_number}"
                    )

                    continue

                if frequency not in VALID_FREQUENCIES:

                    issues.append(
                        f"Invalid frequency :: "
                        f"{portfolio_file.name}:{line_number}"
                    )

                if ticker not in registry_tickers:

                    issues.append(
                        f"Ticker missing from registry :: "
                        f"{ticker}"
                    )

                if shares < 0:

                    issues.append(
                        f"Negative shares :: "
                        f"{portfolio_file.name}:{line_number}"
                    )

                if dividend < 0:

                    issues.append(
                        f"Negative dividend :: "
                        f"{portfolio_file.name}:{line_number}"
                    )

            print(
                f"{portfolio_file.name:<25} "
                f"OK ({row_count} rows)"
            )

    except Exception as error:

        print(f"{portfolio_file.name:<25} ERROR")
        issues.append(str(error))

print(subdivider)

#
# FINAL RESULT
#

print("\nINTEGRITY RESULT:\n")
print(subdivider)

if not issues:

    print("[SYSTEM INTEGRITY] PASS")

else:

    print("[SYSTEM INTEGRITY] FAIL")

    print("\nISSUES FOUND:\n")

    for issue in issues:

        print(f"- {issue}")

print(subdivider)
print(divider)
print("END INTEGRITY CHECK")
print(divider)

if issues:

    sys.exit(1)
