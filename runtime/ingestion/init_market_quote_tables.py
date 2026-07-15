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
CREATE TABLE IF NOT EXISTS market_quote_snapshots (

    id BIGSERIAL PRIMARY KEY,

    ticker TEXT NOT NULL,

    current_price NUMERIC NOT NULL,

    open_price NUMERIC,

    high_price NUMERIC,

    low_price NUMERIC,

    previous_close NUMERIC,

    provider_timestamp TIMESTAMPTZ,

    observed_at TIMESTAMPTZ NOT NULL,

    source TEXT NOT NULL

);
"""


CREATE_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS
market_quote_snapshots_ticker_observed_idx

ON market_quote_snapshots (
    ticker,
    observed_at DESC
);
"""


def main() -> None:

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(CREATE_TABLE_SQL)
            cur.execute(CREATE_INDEX_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG MARKET QUOTE TABLE READY")
    print("Table: market_quote_snapshots")
    print("Source Model: LIVE MARKET QUOTES")
    print("Status: ACTIVE")
    print("===================================")


if __name__ == "__main__":
    main()
