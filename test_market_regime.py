from market_regime_engine import MarketRegimeEngine

engine = MarketRegimeEngine()

tests = [

    ["session_london", "volatility_normal", "strong_trend"],
    ["session_london", "volatility_low", "weak_trend"],
    ["session_ny", "volatility_high", "medium_trend"],
]

print()
print("=== MARKET REGIME TEST ===")
print()

for t in tests:

    regime = engine.detect(t)

    print(t, "→", regime)

print()