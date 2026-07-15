import csv
import os
import psycopg

from datetime import datetime, timezone
from pathlib import Path

DATA_PATH = Path("/data/market/mock_market_data.csv")
LOG_PATH = Path("/runtime/logs/market_ingestion.log")

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

INSERT_SQL = """
INSERT INTO market_ticker_snapshots (

    ticker,
    price,
    dividend_yield,
    frequency,
    snapshot_timestamp

)
VALUES (%s, %s, %s, %s, %s);
"""

def log(message: str):
    timestamp = datetime.now(timezone.utc).isoformat()

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def ingest_market_data():

    if not DATA_PATH.exists():
        log("Market dataset missing")
        print("ERROR: market dataset not found")
        return

    log("Starting market ingestion")

    snapshot_timestamp = datetime.now(timezone.utc)

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            with DATA_PATH.open("r", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    ticker = row["ticker"]
                    price = float(row["price"])
                    dividend_yield = float(row["dividend_yield"])
                    frequency = row["frequency"]

                    cur.execute(
                        INSERT_SQL,
                        (
                            ticker,
                            price,
                            dividend_yield,
                            frequency,
                            snapshot_timestamp
                        )
                    )

                    print("===================================")
                    print(f"Ticker: {ticker}")
                    print(f"Price: ${price}")
                    print(f"Dividend Yield: {dividend_yield}%")
                    print(f"Frequency: {frequency}")
                    print("Stored In PostgreSQL: YES")
                    print("===================================")

                    log(
                        f"Stored ticker={ticker} "
                        f"price={price} "
                        f"yield={dividend_yield}"
                    )

        conn.commit()

    log("Market ingestion completed")

if __name__ == "__main__":
    ingest_market_data()
