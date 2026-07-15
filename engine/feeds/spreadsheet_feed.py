import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SPREADSHEET_FEED = (
    BASE_DIR /
    "data" /
    "feeds" /
    "spreadsheets" /
    "spreadsheet_feed.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: SPREADSHEET FEED")
print(divider)

if not SPREADSHEET_FEED.exists():

    print("\n[ERROR] Spreadsheet feed missing.")
    raise SystemExit(1)

with open(
    SPREADSHEET_FEED,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nSPREADSHEET FEED ENTRIES:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'YIELD':<10}"
    f"{'PAYOUT':<15}"
    f"{'PRICE':<12}"
    f"{'SOURCE':<20}"
)

print(subdivider)

valid_rows = 0

for row in rows:

    ticker = row.get("ticker") or "UNKNOWN"
    dividend_yield = row.get("dividend_yield") or "0.00"
    payout_frequency = row.get("payout_frequency") or "UNKNOWN"
    share_price = row.get("share_price") or "0.00"
    source = row.get("source") or "UNSET"

    if ticker != "UNKNOWN":

        valid_rows += 1

    print(
        f"{ticker:<10}"
        f"{dividend_yield + '%':<10}"
        f"{payout_frequency:<15}"
        f"${share_price:<11}"
        f"{source:<20}"
    )

print(subdivider)

print(
    f"{'VALID FEED ROWS':<30}"
    f"{valid_rows}"
)

print(divider)
print("END SPREADSHEET FEED")
print(divider)
