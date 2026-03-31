# data_loader.py

import requests
import time
import random

API_KEY = "27c818b1a9d842f095736ffcb9f5bd3f"
BASE_URL = "https://api.twelvedata.com/time_series"


def get_candles(symbol, interval, limit=200):
    """
    symbol: EUR/USD
    interval: 15min, 30min, 1h
    """

    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": limit,
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        # --- ERROR HANDLING ---
        if "status" in data and data["status"] == "error":
            print(f"[ERROR] {symbol} {interval}: {data}")
            return _fallback_data(limit)

        values = data.get("values", [])

        if not values:
            print(f"[EMPTY] {symbol} {interval}")
            return _fallback_data(limit)

        candles = []

        for v in reversed(values):  # oldest → newest
            candles.append({
                "open": float(v["open"]),
                "high": float(v["high"]),
                "low": float(v["low"]),
                "close": float(v["close"]),
                "volume": float(v.get("volume", 1))
            })

        return candles

    except Exception as e:
        print(f"[EXCEPTION] {symbol} {interval}: {e}")
        return _fallback_data(limit)


def _fallback_data(n=200):
    """
    Fake data if API fails (щоб pipeline не падав)
    """
    data = []
    price = 1.1000

    for _ in range(n):
        change = random.uniform(-0.002, 0.002)
        open_p = price
        close_p = price + change
        high = max(open_p, close_p) + random.uniform(0, 0.001)
        low = min(open_p, close_p) - random.uniform(0, 0.001)

        data.append({
            "open": open_p,
            "high": high,
            "low": low,
            "close": close_p,
            "volume": random.uniform(100, 1000)
        })

        price = close_p

    return data