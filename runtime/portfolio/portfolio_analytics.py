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
        ticker,
        shares,
        dividend_per_share,
        frequency
    FROM portfolio_positions
    """
)

positions = cursor.fetchall()

print("===================================")
print("DIVAGG PORTFOLIO ANALYTICS")
print("===================================")

total_monthly_income = 0

for position in positions:

    ticker = position[0]
    shares = float(position[1])
    dividend_per_share = float(position[2])
    frequency = position[3]

    annual_dividend = shares * dividend_per_share * 4

    monthly_dividend = annual_dividend / 12

    total_monthly_income += monthly_dividend

    print(f"Ticker: {ticker}")
    print(f"Estimated Monthly Income: ${monthly_dividend:.2f}")
    print("-----------------------------------")

print(f"Total Estimated Monthly Income: ${total_monthly_income:.2f}")

print("===================================")

connection.close()
