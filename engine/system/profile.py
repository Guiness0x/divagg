import csv
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PORTFOLIO_DIR = BASE_DIR / "data" / "portfolios"
REGISTRY_FILE = BASE_DIR / "data" / "registry" / "tickers.csv"

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: RUNTIME PROFILE")
print(divider)

#
# Registry Timing
#

registry_start = time.perf_counter()

registry_rows = 0

with open(REGISTRY_FILE, newline="") as csvfile:

    reader = csv.DictReader(csvfile)

    for _ in reader:

        registry_rows += 1

registry_end = time.perf_counter()

registry_time = (
    registry_end - registry_start
)

#
# Portfolio Timing
#

portfolio_start = time.perf_counter()

portfolio_files = sorted(
    PORTFOLIO_DIR.glob("*.csv")
)

portfolio_rows = 0

for portfolio_file in portfolio_files:

    with open(portfolio_file, newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for _ in reader:

            portfolio_rows += 1

portfolio_end = time.perf_counter()

portfolio_time = (
    portfolio_end - portfolio_start
)

#
# Combined Timing
#

total_time = (
    registry_time +
    portfolio_time
)

#
# Output
#

print("\nRUNTIME METRICS:\n")

print(subdivider)

print(
    f"{'REGISTRY ROWS':<30}"
    f"{registry_rows}"
)

print(
    f"{'PORTFOLIO ROWS':<30}"
    f"{portfolio_rows}"
)

print(
    f"{'PORTFOLIO FILES':<30}"
    f"{len(portfolio_files)}"
)

print(subdivider)

print(
    f"{'REGISTRY LOAD':<30}"
    f"{registry_time:.6f}s"
)

print(
    f"{'PORTFOLIO SCAN':<30}"
    f"{portfolio_time:.6f}s"
)

print(
    f"{'TOTAL RUNTIME':<30}"
    f"{total_time:.6f}s"
)

print(subdivider)

print(divider)
print("END PROFILE")
print(divider)
