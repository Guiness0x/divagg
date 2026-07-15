import csv

from pathlib import Path
from datetime import datetime
from datetime import timezone

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
print("DIVAGG :: ENRICH REGISTRY")
print(divider)

if not LIVE_REGISTRY.exists():

    print("\n[ERROR] Live registry missing.")
    raise SystemExit(1)

#
# Simulated Runtime Enrichment
#
# Generation 0.2 bootstrap layer
#

enrichment_data = {

    "SCHD": {
        "dividend_yield": "3.67",
        "share_price": "81.42",
        "expense_ratio": "0.06",
        "market_cap": "62000000000"
    },

    "VYM": {
        "dividend_yield": "2.89",
        "share_price": "128.11",
        "expense_ratio": "0.06",
        "market_cap": "59000000000"
    },

    "JEPI": {
        "dividend_yield": "7.12",
        "share_price": "56.82",
        "expense_ratio": "0.35",
        "market_cap": "39000000000"
    },

    "JEPQ": {
        "dividend_yield": "8.01",
        "share_price": "49.77",
        "expense_ratio": "0.35",
        "market_cap": "21000000000"
    },

    "O": {
        "dividend_yield": "5.44",
        "share_price": "61.03",
        "expense_ratio": "0.00",
        "market_cap": "52000000000"
    },

    "PLD": {
        "dividend_yield": "2.71",
        "share_price": "112.88",
        "expense_ratio": "0.00",
        "market_cap": "104000000000"
    },

    "DLR": {
        "dividend_yield": "3.22",
        "share_price": "145.67",
        "expense_ratio": "0.00",
        "market_cap": "48000000000"
    },

    "KO": {
        "dividend_yield": "3.12",
        "share_price": "68.14",
        "expense_ratio": "0.00",
        "market_cap": "294000000000"
    }
}

rows = []

with open(
    LIVE_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    reader = csv.DictReader(csvfile)

    fieldnames = reader.fieldnames

    for row in reader:

        if not row:

            continue

        ticker = (
            row.get("ticker")
        )

        if not ticker:

            continue

        enrichment = (
            enrichment_data.get(
                ticker
            )
        )

        if enrichment:

            row.update(enrichment)

            row["source"] = (
                "runtime_enrichment"
            )

            row["last_updated"] = (
                datetime.now(
                    timezone.utc
                ).isoformat()
            )

        rows.append(row)

with open(
    LIVE_REGISTRY,
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(rows)

print("\nREGISTRY ENRICHMENT:\n")

print(subdivider)

print(
    f"{'ENRICHED ENTRIES':<30}"
    f"{len(rows)}"
)

print(
    f"{'ENRICHMENT SOURCE':<30}"
    f"runtime_enrichment"
)

print(subdivider)

print(divider)
print("END ENRICH REGISTRY")
print(divider)
