import os
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

cursor.execute(
    """
    SELECT
        snapshot_timestamp,
        total_monthly_income,
        total_positions
    FROM portfolio_snapshots
    ORDER BY snapshot_timestamp ASC
    """
)

snapshots = cursor.fetchall()

print("===================================")
print("DIVAGG SNAPSHOT ANALYTICS")
print("===================================")

for snapshot in snapshots:

    timestamp = snapshot[0]
    monthly_income = float(snapshot[1])
    total_positions = snapshot[2]

    print(f"Snapshot Timestamp: {timestamp}")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print(f"Total Positions: {total_positions}")
    print("-----------------------------------")

print(f"Total Snapshots: {len(snapshots)}")

print("===================================")

connection.close()
