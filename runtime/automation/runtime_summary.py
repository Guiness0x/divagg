import os
import psycopg

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

QUERIES = {

    "reconciliation_events": """
    SELECT COUNT(*)
    FROM reconciliation_events;
    """,

    "high_severity_events": """
    SELECT COUNT(*)
    FROM reconciliation_events
    WHERE severity_level = 'HIGH';
    """,

    "detected_anomalies": """
    SELECT COUNT(DISTINCT ticker)
    FROM reconciliation_events
    WHERE severity_level = 'HIGH';
    """,

    "successful_runtime_cycles": """
    SELECT COUNT(*)
    FROM runtime_cycle_events
    WHERE cycle_status = 'SUCCESS';
    """
}

def fetch_metric(cur, query):

    cur.execute(query)

    return cur.fetchone()[0]

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            reconciliation_events = fetch_metric(
                cur,
                QUERIES["reconciliation_events"]
            )

            high_severity_events = fetch_metric(
                cur,
                QUERIES["high_severity_events"]
            )

            detected_anomalies = fetch_metric(
                cur,
                QUERIES["detected_anomalies"]
            )

            successful_runtime_cycles = fetch_metric(
                cur,
                QUERIES["successful_runtime_cycles"]
            )

    print("===================================")
    print("DIVAGG OPERATIONAL SUMMARY")
    print("===================================")

    print(
        f"Reconciliation Events: "
        f"{reconciliation_events}"
    )

    print(
        f"HIGH Severity Events: "
        f"{high_severity_events}"
    )

    print(
        f"Detected Anomalies: "
        f"{detected_anomalies}"
    )

    print(
        f"Successful Runtime Cycles: "
        f"{successful_runtime_cycles}"
    )

    print("===================================")
    print("Operational Status: ACTIVE")
    print("===================================")

if __name__ == "__main__":
    main()
