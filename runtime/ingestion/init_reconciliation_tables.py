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
CREATE TABLE IF NOT EXISTS reconciliation_events (

    id SERIAL PRIMARY KEY,

    ticker TEXT NOT NULL,

    internal_dividend NUMERIC NOT NULL,

    market_estimated_dividend NUMERIC NOT NULL,

    dividend_delta NUMERIC NOT NULL,

    internal_frequency TEXT NOT NULL,

    market_frequency TEXT NOT NULL,

    reconciliation_status TEXT NOT NULL,

    event_timestamp TIMESTAMPTZ NOT NULL

);
"""

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(CREATE_TABLE_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG RECONCILIATION TABLE READY")
    print("Table: reconciliation_events")
    print("Status: ACTIVE")
    print("===================================")

if __name__ == "__main__":
    main()
