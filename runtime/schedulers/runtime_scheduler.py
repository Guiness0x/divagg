import time
import os
import subprocess
from datetime import datetime, UTC

import psycopg

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

connection = psycopg.connect(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    dbname=POSTGRES_DB
)

cursor = connection.cursor()

cycle_count = 0

while True:

    timestamp = datetime.now(UTC)

    scheduler_status = "ACTIVE"

    runtime_cycle = f"EXECUTED_{cycle_count}"

    log_entry = f"""
===================================
DIVAGG SCHEDULER CYCLE
===================================
Timestamp: {timestamp}
Scheduler Status: {scheduler_status}
Runtime Cycle: {runtime_cycle}
===================================
"""

    print(log_entry)

    with open("/runtime/logs/scheduler.log", "a") as log:
        log.write(log_entry + "\n")

    cursor.execute(
        """
        INSERT INTO runtime_cycles (
            cycle_timestamp,
            scheduler_status,
            runtime_cycle
        )
        VALUES (%s, %s, %s)
        """,
        (
            timestamp,
            scheduler_status,
            runtime_cycle
        )
    )

    connection.commit()

    print("===================================")
    print("DIVAGG FINANCIAL COGNITION START")
    print("===================================")

    subprocess.run(
        ["python", "/runtime/portfolio/financial_cognition_cycle.py"],
        check=True
    )

    print("===================================")
    print("DIVAGG FINANCIAL COGNITION END")
    print("===================================")

    cycle_count += 1

    time.sleep(60)
