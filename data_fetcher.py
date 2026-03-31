# data_fetcher.py

import requests
import time

API_KEY = "27c818b1a9d842f095736ffcb9f5bd3f"
BASE_URL = "https://api.twelvedata.com/time_series"

# кеш з TTL
CACHE = {}
CACHE_TTL = 60  # секунд


def get_candles(symbol, interval):
    key = f"{symbol}_{interval}"

    now = time.time()

    # --- CACHE WITH TTL ---
    if key in CACHE:
        data, ts = CACHE[key]

        if now - ts < CACHE_TTL:
            return data

    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": 200,
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if "values" not in data:
            raise Exception(data)

        candles = list(reversed(data["values"]))

        # кешуємо з timestamp
        CACHE[key] = (candles, now)

        time.sleep(1.2)

        return candles

    except Exception as e:
        print(f"[FETCH ERROR] {symbol} {interval}: {e}")
        return []