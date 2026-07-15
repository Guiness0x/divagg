import csv
import sys

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: PORTFOLIO LIST")
print(divider)

print(f"\nACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}")

if not PORTFOLIO_FILE.exists():

    print(f"\n[ERROR] Portfolio not found:")
    print(PORTFOLIO_FILE)

    sys.exit(1)

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        table_header = (
            f"{'TICKER':<10}"
            f"{'SHARES':>10}"
            f"{'DIVIDEND':>15}"
            f"{'FREQ':>15}"
        )

        print("")
        print(table_header)
        print(subdivider)

        row_count = 0

        for row in reader:

            ticker = row['ticker']
            shares = row['shares']
            dividend = row['dividend']
            frequency = row['frequency']

            output_line = (
                f"{ticker:<10}"
                f"{shares:>10}"
                f"{dividend:>15}"
                f"{frequency:>15}"
            )

            print(output_line)

            row_count += 1

        print(subdivider)
        print(f"TOTAL POSITIONS : {row_count}")

except Exception as error:

    print(f"[ERROR] {error}")
    sys.exit(1)

print(divider)
print("END PORTFOLIO LIST")
print(divider)
