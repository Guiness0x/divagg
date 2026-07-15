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
print("DIVAGG SNAPSHOT DELTA ANALYTICS")
print("===================================")

if len(snapshots) < 2:

    print("Not enough snapshots for delta analysis.")

else:

    previous_snapshot = snapshots[-2]
    current_snapshot = snapshots[-1]

    previous_income = float(previous_snapshot[1])
    current_income = float(current_snapshot[1])

    income_delta = current_income - previous_income

    previous_positions = previous_snapshot[2]
    current_positions = current_snapshot[2]

    position_delta = current_positions - previous_positions

    print(f"Previous Monthly Income: ${previous_income:.2f}")
    print(f"Current Monthly Income: ${current_income:.2f}")
    print(f"Income Delta: ${income_delta:.2f}")

    print("-----------------------------------")

    print(f"Previous Positions: {previous_positions}")
    print(f"Current Positions: {current_positions}")
    print(f"Position Delta: {position_delta}")

print("===================================")

connection.close()
