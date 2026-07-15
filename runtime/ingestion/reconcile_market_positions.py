import os
import psycopg

from datetime import datetime, timezone

DATABASE_CONFIG = {
    "host": os.environ["POSTGRES_HOST"],
    "port": os.environ["POSTGRES_PORT"],
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}

QUERY = """
SELECT DISTINCT ON (m.ticker)

    p.ticker,
    p.dividend_per_share,
    p.frequency,

    m.price,
    m.dividend_yield,
    m.frequency,
    m.snapshot_timestamp

FROM portfolio_positions p

JOIN market_ticker_snapshots m
ON p.ticker = m.ticker

ORDER BY m.ticker, m.snapshot_timestamp DESC;
"""

INSERT_SQL = """
INSERT INTO reconciliation_events (

    ticker,
    internal_dividend,
    market_estimated_dividend,
    dividend_delta,
    internal_frequency,
    market_frequency,
    reconciliation_status,
    event_timestamp,
    severity_level

)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

def normalize_frequency(value: str) -> str:
    return value.strip().lower()

def classify_severity(delta: float) -> str:
    absolute_delta = abs(delta)

    if absolute_delta < 1:
        return "LOW"

    if absolute_delta < 3:
        return "MEDIUM"

    return "HIGH"

def main():

    with psycopg.connect(**DATABASE_CONFIG) as conn:

        with conn.cursor() as cur:

            cur.execute(QUERY)

            rows = cur.fetchall()

            print("===================================")
            print("DIVAGG RECONCILIATION ANALYSIS")
            print("===================================")

            for row in rows:

                ticker = row[0]

                internal_dividend = float(row[1])
                internal_frequency = normalize_frequency(row[2])

                market_price = float(row[3])
                market_yield = float(row[4])
                market_frequency = normalize_frequency(row[5])

                estimated_market_dividend = (
                    market_price * (market_yield / 100)
                )

                delta = (
                    estimated_market_dividend
                    - internal_dividend
                )

                if internal_frequency != market_frequency:
                    reconciliation_status = "MISMATCH"
                else:
                    reconciliation_status = "OK"

                severity_level = classify_severity(delta)

                cur.execute(
                    INSERT_SQL,
                    (
                        ticker,
                        internal_dividend,
                        estimated_market_dividend,
                        delta,
                        internal_frequency,
                        market_frequency,
                        reconciliation_status,
                        datetime.now(timezone.utc),
                        severity_level
                    )
                )

                print(f"Ticker: {ticker}")
                print("-----------------------------------")
                print(f"Internal Dividend: ${internal_dividend:.4f}")
                print(
                    f"Market Estimated Dividend: "
                    f"${estimated_market_dividend:.4f}"
                )
                print(f"Dividend Delta: ${delta:.4f}")
                print("")
                print(f"Internal Frequency: {internal_frequency}")
                print(f"Market Frequency: {market_frequency}")
                print(
                    f"Reconciliation Status: "
                    f"{reconciliation_status}"
                )
                print(f"Severity Level: {severity_level}")
                print("===================================")

        conn.commit()

if __name__ == "__main__":
    main()
