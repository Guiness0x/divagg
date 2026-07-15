import json
import os
import urllib.error
import urllib.parse
import urllib.request

from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from typing import Any

import psycopg


API_KEY = os.environ["FINNHUB_API_KEY"]
BASE_URL = "https://finnhub.io/api/v1/quote"
SOURCE_NAME = "finnhub"

SYMBOLS = [
    "SCHD",
    "JEPI",
    "O",
    "MAIN",
]

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

INSERT_SQL = """
INSERT INTO market_quote_snapshots (
    ticker,
    current_price,
    open_price,
    high_price,
    low_price,
    previous_close,
    provider_timestamp,
    observed_at,
    source
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""


def fetch_quote(symbol: str) -> dict[str, Any]:
    query = urllib.parse.urlencode(
        {
            "symbol": symbol,
            "token": API_KEY,
        }
    )

    url = f"{BASE_URL}?{query}"

    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "DIVAGG/1.0",
        },
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        payload = response.read().decode("utf-8")

    return json.loads(payload)


def normalize_decimal(value: Any) -> Decimal | None:
    if value is None:
        return None

    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        return None


def normalize_provider_timestamp(value: Any) -> datetime | None:
    if value in (None, 0, "0"):
        return None

    try:
        return datetime.fromtimestamp(
            int(value),
            tz=timezone.utc,
        )
    except (TypeError, ValueError, OverflowError):
        return None


def ingest_symbol(
    cur: psycopg.Cursor,
    symbol: str,
    observed_at: datetime,
) -> bool:
    try:
        quote = fetch_quote(symbol)
    except urllib.error.HTTPError as error:
        print(f"Ticker: {symbol}")
        print(f"Status: FAILED - HTTP {error.code}")
        print("===================================")
        return False
    except urllib.error.URLError as error:
        print(f"Ticker: {symbol}")
        print(f"Status: FAILED - {error.reason}")
        print("===================================")
        return False
    except (TimeoutError, json.JSONDecodeError) as error:
        print(f"Ticker: {symbol}")
        print(f"Status: FAILED - {error}")
        print("===================================")
        return False

    current_price = normalize_decimal(quote.get("c"))

    if current_price is None or current_price <= 0:
        print(f"Ticker: {symbol}")
        print("Status: SKIPPED - invalid current price")
        print("===================================")
        return False

    open_price = normalize_decimal(quote.get("o"))
    high_price = normalize_decimal(quote.get("h"))
    low_price = normalize_decimal(quote.get("l"))
    previous_close = normalize_decimal(quote.get("pc"))

    provider_timestamp = normalize_provider_timestamp(
        quote.get("t")
    )

    cur.execute(
        INSERT_SQL,
        (
            symbol,
            current_price,
            open_price,
            high_price,
            low_price,
            previous_close,
            provider_timestamp,
            observed_at,
            SOURCE_NAME,
        ),
    )

    print(f"Ticker: {symbol}")
    print(f"Current Price: ${current_price}")
    print(f"Open Price: ${open_price}")
    print(f"High Price: ${high_price}")
    print(f"Low Price: ${low_price}")
    print(f"Previous Close: ${previous_close}")
    print(f"Provider Timestamp: {provider_timestamp}")
    print(f"Observed At: {observed_at}")
    print(f"Source: {SOURCE_NAME}")
    print("Stored In PostgreSQL: YES")
    print("===================================")

    return True


def main() -> None:
    observed_at = datetime.now(timezone.utc)

    stored_count = 0
    failed_count = 0

    print("===================================")
    print("DIVAGG FINNHUB MARKET OBSERVATION")
    print("===================================")

    with psycopg.connect(**DATABASE_CONFIG) as conn:
        with conn.cursor() as cur:
            for symbol in SYMBOLS:
                stored = ingest_symbol(
                    cur,
                    symbol,
                    observed_at,
                )

                if stored:
                    stored_count += 1
                else:
                    failed_count += 1

        conn.commit()

    print("===================================")
    print("DIVAGG MARKET INGESTION COMPLETE")
    print(f"Stored Snapshots: {stored_count}")
    print(f"Failed Snapshots: {failed_count}")
    print("Status: SUCCESS" if failed_count == 0 else "Status: PARTIAL")
    print("===================================")


if __name__ == "__main__":
    main()
