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

ticker = "O"
shares = 30
dividend_per_share = 0.26
frequency = "MONTHLY"

created_at = datetime.now(UTC)

cursor.execute(
    """
    INSERT INTO portfolio_positions (
        ticker,
        shares,
        dividend_per_share,
        frequency,
        created_at
    )
    VALUES (%s, %s, %s, %s, %s)
    """,
    (
        ticker,
        shares,
        dividend_per_share,
        frequency,
        created_at
    )
)

connection.commit()

print("===================================")
print("DIVAGG POSITION INSERTED")
print("===================================")
print(f"Ticker: {ticker}")
print(f"Shares: {shares}")
print(f"Dividend Per Share: {dividend_per_share}")
print(f"Frequency: {frequency}")
print("===================================")

connection.close()
