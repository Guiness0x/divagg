from pathlib import Path
import re
import sys

PORTFOLIO_DIR = Path("../data/portfolios")

divider = "=" * 60

print(divider)
print("DIVAGG :: CREATE PORTFOLIO")
print(divider)

portfolio_name = input(
    "\nPortfolio name : "
).strip().lower()

#
# Validation
#

if not portfolio_name:

    print("\n[ERROR] Portfolio name cannot be empty.")
    sys.exit(1)

if not re.match(r"^[a-z0-9_]+$", portfolio_name):

    print("\n[ERROR] Invalid portfolio name.")
    print("Use lowercase letters, numbers, and underscores only.")

    sys.exit(1)

portfolio_file = (
    PORTFOLIO_DIR /
    f"{portfolio_name}.csv"
)

if portfolio_file.exists():

    print("\n[ERROR] Portfolio already exists.")
    sys.exit(1)

#
# Create Portfolio
#

try:

    with open(portfolio_file, "w") as file:

        file.write(
            "ticker,shares,dividend,frequency\n"
        )

    print("\n[SUCCESS] Portfolio created.")
    print(f"FILE : {portfolio_file.name}")

except Exception as error:

    print(f"\n[ERROR] Failed to create portfolio :: {error}")
    sys.exit(1)

print(f"\n{divider}")
print("END CREATE")
print(divider)
