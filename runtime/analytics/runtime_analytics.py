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
    SELECT COUNT(*)
    FROM runtime_cycles
    """
)

total_cycles = cursor.fetchone()[0]

print("===================================")
print("DIVAGG RUNTIME ANALYTICS")
print("===================================")
print(f"Total Runtime Cycles: {total_cycles}")
print("===================================")

connection.close()
