import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LIVE_REGISTRY = (
    BASE_DIR /
    "data" /
    "live" /
    "live_registry.csv"
)

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: REGISTRY OVERVIEW")
print(divider)

if not LIVE_REGISTRY.exists():

    print("\n[ERROR] Live registry missing.")
    raise SystemExit(1)

rows = []

with open(
    LIVE_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        if not row:

            continue

        ticker = (
            row.get("ticker")
        )

        if not ticker:

            continue

        rows.append(row)

print("\nLIVE FINANCIAL STATE:\n")

print(subdivider)

print(
    f"{'TICKER':<10}"
    f"{'YIELD':<10}"
    f"{'PRICE':<12}"
    f"{'PAYOUT':<15}"
    f"{'TYPE':<18}"
)

print(subdivider)

for row in rows:

    ticker = (
        row.get("ticker")
        or "UNKNOWN"
    )

    dividend_yield = (
        row.get("dividend_yield")
        or "0.00"
    )

    share_price = (
        row.get("share_price")
        or "0.00"
    )

    payout_frequency = (
        row.get("payout_frequency")
        or "UNKNOWN"
    )

    asset_type = (
        row.get("asset_type")
        or "UNKNOWN"
    )

    print(
        f"{ticker:<10}"
        f"{dividend_yield + '%':<10}"
        f"${share_price:<11}"
        f"{payout_frequency:<15}"
        f"{asset_type:<18}"
    )

print(subdivider)

#
# Runtime Totals
#

total_entries = len(rows)

etf_count = len(
    [
        row for row in rows
        if row.get("asset_type")
        in [
            "dividend_etf",
            "income_fund"
        ]
    ]
)

reit_count = len(
    [
        row for row in rows
        if row.get("asset_type")
        == "reit"
    ]
)

equity_count = len(
    [
        row for row in rows
        if row.get("asset_type")
        == "equity"
    ]
)

print(
    f"{'TOTAL ENTRIES':<30}"
    f"{total_entries}"
)

print(
    f"{'ETF / INCOME FUNDS':<30}"
    f"{etf_count}"
)

print(
    f"{'REITS':<30}"
    f"{reit_count}"
)

print(
    f"{'EQUITIES':<30}"
    f"{equity_count}"
)

print(divider)
print("END REGISTRY OVERVIEW")
print(divider)
