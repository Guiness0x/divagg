import os
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

cursor.execute(
    """
    SELECT
        ticker,
        shares,
        dividend_per_share,
        frequency
    FROM portfolio_positions
    """
)

positions = cursor.fetchall()

total_monthly_income = 0

for position in positions:

    shares = float(position[1])
    dividend_per_share = float(position[2])

    annual_dividend = shares * dividend_per_share * 4

    monthly_dividend = annual_dividend / 12

    total_monthly_income += monthly_dividend

total_positions = len(positions)

snapshot_timestamp = datetime.now(UTC)

cursor.execute(
    """
    INSERT INTO portfolio_snapshots (
        snapshot_timestamp,
        total_monthly_income,
        total_positions
    )
    VALUES (%s, %s, %s)
    """,
    (
        snapshot_timestamp,
        total_monthly_income,
        total_positions
    )
)

connection.commit()

print("===================================")
print("DIVAGG SNAPSHOT CREATED")
print("===================================")
print(f"Snapshot Timestamp: {snapshot_timestamp}")
print(f"Total Monthly Income: ${total_monthly_income:.2f}")
print(f"Total Positions: {total_positions}")
print("===================================")

connection.close()
