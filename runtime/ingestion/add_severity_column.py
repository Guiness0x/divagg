import os
import psycopg

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

ALTER_SQL = """
ALTER TABLE reconciliation_events
ADD COLUMN IF NOT EXISTS severity_level TEXT;
"""

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(ALTER_SQL)

        conn.commit()

    print("===================================")
    print("DIVAGG SEVERITY COLUMN ADDED")
    print("Column: severity_level")
    print("Status: ACTIVE")
    print("===================================")

if __name__ == "__main__":
    main()
