import os
import psycopg

from collections import defaultdict

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

QUERY = """
SELECT
    ticker,
    price,
    dividend_yield,
    frequency,
    snapshot_timestamp
FROM market_ticker_snapshots
ORDER BY ticker, snapshot_timestamp ASC;
"""

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(QUERY)

            rows = cur.fetchall()

    grouped = defaultdict(list)

    for row in rows:
        grouped[row[0]].append(row)

    print("===================================")
    print("DIVAGG MARKET DELTA ANALYSIS")
    print("===================================")

    for ticker, snapshots in grouped.items():

        if len(snapshots) < 2:
            continue

        previous = snapshots[-2]
        current = snapshots[-1]

        previous_price = float(previous[1])
        current_price = float(current[1])

        previous_yield = float(previous[2])
        current_yield = float(current[2])

        price_delta = current_price - previous_price
        yield_delta = current_yield - previous_yield

        print(f"Ticker: {ticker}")
        print("-----------------------------------")
        print(f"Previous Price: ${previous_price:.2f}")
        print(f"Current Price: ${current_price:.2f}")
        print(f"Price Delta: ${price_delta:.2f}")
        print("")
        print(f"Previous Yield: {previous_yield:.2f}%")
        print(f"Current Yield: {current_yield:.2f}%")
        print(f"Yield Delta: {yield_delta:.2f}%")
        print("===================================")

if __name__ == "__main__":
    main()
