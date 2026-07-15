import os
import subprocess
import psycopg

from datetime import datetime, timezone

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

RUNTIME_TASKS = [

    (
        "Market Ingestion",
        "/runtime/ingestion/ingest_market_data.py"
    ),

    (
        "Reconciliation Analysis",
        "/runtime/ingestion/reconcile_market_positions.py"
    ),

    (
        "Anomaly Scan",
        "/runtime/ingestion/anomaly_scan.py"
    ),
]

INSERT_SQL = """
INSERT INTO runtime_cycle_events (

    cycle_name,
    cycle_status,
    started_at,
    completed_at

)
VALUES (%s, %s, %s, %s);
"""

def persist_runtime_cycle(
    started_at,
    completed_at,
    cycle_status
):

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(
                INSERT_SQL,
                (
                    "DIVAGG_AUTONOMOUS_RUNTIME",
                    cycle_status,
                    started_at,
                    completed_at
                )
            )

        conn.commit()

def run_task(task_name: str, task_path: str):

    print("===================================")
    print(f"RUNNING TASK: {task_name}")
    print("===================================")

    result = subprocess.run(
        ["python", task_path],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print("ERROR OUTPUT:")
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(
            f"Task failed: {task_name}"
        )

def main():

    started_at = datetime.now(timezone.utc)

    print("===================================")
    print("DIVAGG AUTONOMOUS RUNTIME CYCLE")
    print("===================================")

    cycle_status = "SUCCESS"

    try:

        for task_name, task_path in RUNTIME_TASKS:
            run_task(task_name, task_path)

    except Exception as error:

        cycle_status = "FAILURE"

        print("===================================")
        print("RUNTIME FAILURE DETECTED")
        print(f"ERROR: {error}")
        print("===================================")

    completed_at = datetime.now(timezone.utc)

    persist_runtime_cycle(
        started_at,
        completed_at,
        cycle_status
    )

    print("===================================")
    print("DIVAGG RUNTIME CYCLE COMPLETE")
    print(f"Status: {cycle_status}")
    print("===================================")

if __name__ == "__main__":
    main()
