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
CREATE TABLE IF NOT EXISTS dividend_snapshots (

    id BIGSERIAL PRIMARY KEY,

    ticker TEXT NOT NULL,

    dividend_amount NUMERIC NOT NULL,

    dividend_yield NUMERIC,

    payment_frequency TEXT,

    declaration_date DATE,

    ex_dividend_date DATE,

    record_date DATE,

    payment_date DATE,

    provider_timestamp TIMESTAMPTZ,

    observed_at TIMESTAMPTZ NOT NULL,

    source TEXT NOT NULL

);
"""


CREATE_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS
dividend_snapshots_ticker_observed_idx

ON dividend_snapshots (
    ticker,
    observed_at DESC
);
"""


CREATE_EX_DATE_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS
dividend_snapshots_ex_date_idx

ON dividend_snapshots (
    ex_dividend_date
);
"""


def main() -> None:

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(CREATE_TABLE_SQL)
            cur.execute(CREATE_INDEX_SQL)
            cur.execute(CREATE_EX_DATE_INDEX_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG DIVIDEND TABLE READY")
    print("Table: dividend_snapshots")
    print("Source Model: DIVIDEND OBSERVATION")
    print("Status: ACTIVE")
    print("===================================")


if __name__ == "__main__":
    main()
