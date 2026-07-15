import os
import psycopg

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
    severity_level,
    COUNT(*) as severity_count

FROM reconciliation_events

WHERE severity_level = 'HIGH'

GROUP BY ticker, severity_level

HAVING COUNT(*) >= 3

ORDER BY severity_count DESC;
"""

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(QUERY)

            rows = cur.fetchall()

    print("===================================")
    print("DIVAGG ANOMALY SCAN")
    print("===================================")

    if not rows:
        print("No anomalies detected")
        print("===================================")
        return

    for row in rows:

        ticker = row[0]
        severity = row[1]
        count = row[2]

        print(f"Ticker: {ticker}")
        print(f"Severity: {severity}")
        print(f"Repeated Events: {count}")
        print("Anomaly Status: DETECTED")
        print("===================================")

if __name__ == "__main__":
    main()
