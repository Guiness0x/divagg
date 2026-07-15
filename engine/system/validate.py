import csv
import sys

INPUT_FILE = "../data/portfolio.csv"

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

valid_rows = 0
invalid_rows = 0

divider = "=" * 60

print(divider)
print("DIVAGG :: DATA VALIDATION")
print(divider)

try:

    with open(INPUT_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for line_number, row in enumerate(reader, start=2):

            try:

                ticker = row['ticker'].strip()
                shares = float(row['shares'])
                dividend = float(row['dividend'])
                frequency = row['frequency'].strip().lower()

                if not ticker:
                    raise ValueError("Missing ticker")

                if shares < 0:
                    raise ValueError("Negative shares")

                if dividend < 0:
                    raise ValueError("Negative dividend")

                if frequency not in VALID_FREQUENCIES:
                    raise ValueError("Invalid frequency")

                valid_rows += 1

                print(
                    f"[VALID] "
                    f"Line {line_number} :: "
                    f"{ticker}"
                )

            except Exception as row_error:

                invalid_rows += 1

                print(
                    f"[INVALID] "
                    f"Line {line_number} :: "
                    f"{row_error}"
                )

except FileNotFoundError:

    print(f"[ERROR] Missing file: {INPUT_FILE}")
    sys.exit(1)

except Exception as error:

    print(f"[ERROR] {error}")
    sys.exit(1)

print("\n" + "-" * 60)

print(f"VALID ROWS   : {valid_rows}")
print(f"INVALID ROWS : {invalid_rows}")

print(divider)
print("END VALIDATION")
print(divider)
