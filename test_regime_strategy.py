from regime_strategy_engine import RegimeStrategyEngine

engine = RegimeStrategyEngine()

pattern = [
    "normal_volume",
    "pullback",
    "trend_market"
]

context = [
    "session_london",
    "volatility_normal",
    "strong_trend"
]

matches = engine.match_strategy(pattern, context)

print()
print("=== REGIME STRATEGY MATCH ===")
print()

for m in matches:

    print(
        "pattern:", m["pattern"],
        "| direction:", m["direction"],
        "| risk:", m["risk"],
        "| regime:", m["regime"]
    )

print()