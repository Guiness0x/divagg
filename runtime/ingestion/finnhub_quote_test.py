import os
import json
import urllib.request
import urllib.parse

API_KEY = os.environ["FINNHUB_API_KEY"]
BASE_URL = "https://finnhub.io/api/v1/quote"

SYMBOL = "SCHD"

def fetch_quote(symbol: str):

    query = urllib.parse.urlencode(
        {
            "symbol": symbol,
            "token": API_KEY,
        }
    )

    url = f"{BASE_URL}?{query}"

    with urllib.request.urlopen(url, timeout=15) as response:
        payload = response.read().decode("utf-8")

    return json.loads(payload)

def main():

    quote = fetch_quote(SYMBOL)

    print("===================================")
    print("DIVAGG LIVE FINNHUB QUOTE TEST")
    print("===================================")
    print(f"Symbol: {SYMBOL}")
    print(f"Current Price: {quote.get('c')}")
    print(f"Open Price: {quote.get('o')}")
    print(f"High Price: {quote.get('h')}")
    print(f"Low Price: {quote.get('l')}")
    print(f"Previous Close: {quote.get('pc')}")
    print(f"Timestamp: {quote.get('t')}")
    print("===================================")

if __name__ == "__main__":
    main()
