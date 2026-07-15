import os
import psycopg

from datetime import datetime, timezone
from pathlib import Path

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

REPORT_DIRECTORY = Path(
    "/runtime/reports"
)

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

def build_report():

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

    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y%m%d_%H%M%S")

    REPORT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    report_path = (
        REPORT_DIRECTORY
        / f"runtime_report_{timestamp}.txt"
    )

    report_contents = f"""
===================================
DIVAGG OPERATIONAL REPORT
===================================

Generated At:
{timestamp}

Reconciliation Events:
{reconciliation_events}

HIGH Severity Events:
{high_severity_events}

Detected Anomalies:
{detected_anomalies}

Successful Runtime Cycles:
{successful_runtime_cycles}

Operational Status:
ACTIVE

===================================
"""

    report_path.write_text(
        report_contents,
        encoding="utf-8"
    )

    print("===================================")
    print("DIVAGG REPORT EXPORT COMPLETE")
    print(f"Report Path: {report_path}")
    print("===================================")

def main():
    build_report()

if __name__ == "__main__":
    main()
