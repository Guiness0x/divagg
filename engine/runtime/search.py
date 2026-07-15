import csv
import sys

INPUT_FILE = "../data/portfolio.csv"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SEARCH PORTFOLIO")
print(divider)

if not INPUT_FILE:

    print("[ERROR] portfolio.csv not found.")
    sys.exit(1)

search_term = input(
    "\nSearch ticker or frequency : "
).strip().lower()

matches = []

try:

    with open(INPUT_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            ticker = row['ticker'].lower()
            frequency = row['frequency'].lower()

            if (
                search_term == ticker or
                search_term == frequency
            ):
                matches.append(row)

except Exception as error:

    print(f"[ERROR] {error}")
    sys.exit(1)

if not matches:

    print("\n[INFO] No matches found.")
    sys.exit(0)

print("\nMATCHES:\n")

table_header = (
    f"{'TICKER':<10}"
    f"{'SHARES':>10}"
    f"{'DIVIDEND':>15}"
    f"{'FREQ':>15}"
)

print(table_header)
print(subdivider)

for row in matches:

    output_line = (
        f"{row['ticker']:<10}"
        f"{row['shares']:>10}"
        f"{row['dividend']:>15}"
        f"{row['frequency']:>15}"
    )

    print(output_line)

print(subdivider)

print(f"TOTAL MATCHES : {len(matches)}")

print(divider)
print("END SEARCH")
print(divider)
