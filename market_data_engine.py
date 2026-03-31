import requests
import time

# =========================
# CONFIG
# =========================

API_KEY = "27c818b1a9d842f095736ffcb9f5bd3f"

PAIRS = {
    "EURUSD": "EUR/USD",
    "GBPUSD": "GBP/USD",
    "AUDUSD": "AUD/USD",
    "USDCAD": "USD/CAD",
    "EURJPY": "EUR/JPY"
}

TIMEFRAMES = {
    "M15": "15min",
    "M30": "30min",
    "H1": "1h"
}

CANDLES_COUNT = 200

REQUEST_DELAY = 8  # секунди між запитами
MAX_RETRIES = 3


# =========================
# FETCH DATA
# =========================

def fetch_candles(symbol, interval):
    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": CANDLES_COUNT,
        "apikey": API_KEY
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            # ❗ RATE LIMIT HANDLING
            if "code" in data and data["code"] == 429:
                print(f"[RATE LIMIT] Waiting... ({symbol} {interval})")
                time.sleep(60)
                continue

            if "values" not in data:
                print(f"[API ERROR] {symbol} {interval}: {data}")
                return []

            candles = []

            for c in reversed(data["values"]):
                try:
                    candles.append({
                        "time": c["datetime"],
                        "open": float(c["open"]),
                        "high": float(c["high"]),
                        "low": float(c["low"]),
                        "close": float(c["close"]),
                        "volume": float(c.get("volume", 0))
                    })
                except:
                    continue

            return candles

        except Exception as e:
            print(f"[ERROR] {symbol} {interval}:", e)
            time.sleep(5)

    return []


# =========================
# LOAD ALL DATA
# =========================

def load_market_data():
    market_data = {}

    for pair, symbol in PAIRS.items():
        print(f"\nLoading {pair}")
        market_data[pair] = {}

        for tf_name, tf in TIMEFRAMES.items():
            candles = fetch_candles(symbol, tf)
            market_data[pair][tf_name] = candles

            print(f"{tf_name}: {len(candles)} candles")

            time.sleep(REQUEST_DELAY)

    return market_data


# =========================
# TEST
# =========================

if __name__ == "__main__":
    print("=== MARKET DATA TEST (FINAL STABLE) ===")

    data = load_market_data()

    print("\n=== FINAL RESULT ===")

    for pair in data:
        print(f"\nPAIR: {pair}")

        for tf in data[pair]:
            print(f"{tf}: {len(data[pair][tf])}")