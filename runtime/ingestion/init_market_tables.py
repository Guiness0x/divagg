import os
import psycopg

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS market_ticker_snapshots (

    id SERIAL PRIMARY KEY,

    ticker TEXT NOT NULL,

    price NUMERIC NOT NULL,

    dividend_yield NUMERIC NOT NULL,

    frequency TEXT NOT NULL,

    snapshot_timestamp TIMESTAMPTZ NOT NULL

);
"""

def main():
    with psycopg.connect(**DATABASE_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG MARKET TABLE INITIALIZED")
    print("Table: market_ticker_snapshots")
    print("Status: READY")
    print("===================================")

if __name__ == "__main__":
    main()
