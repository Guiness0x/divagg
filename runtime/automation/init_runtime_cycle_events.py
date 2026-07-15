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
CREATE TABLE IF NOT EXISTS runtime_cycle_events (

    id SERIAL PRIMARY KEY,

    cycle_name TEXT NOT NULL,

    cycle_status TEXT NOT NULL,

    started_at TIMESTAMPTZ NOT NULL,

    completed_at TIMESTAMPTZ NOT NULL

);
"""

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(CREATE_TABLE_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG RUNTIME EVENT TABLE READY")
    print("Table: runtime_cycle_events")
    print("Status: ACTIVE")
    print("===================================")

if __name__ == "__main__":
    main()
