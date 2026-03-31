from strategy_lifecycle_engine import StrategyLifecycleEngine

engine = StrategyLifecycleEngine()

strategy = {
    "entry_pattern": "normal_volume pullback",
    "direction": "follow_trend",
    "risk_model": "adaptive"
}

engine.register_strategy(strategy)

engine.record_trade("normal_volume pullback", True)
engine.record_trade("normal_volume pullback", False)
engine.record_trade("normal_volume pullback", True)

report = engine.report()

print()
print("=== STRATEGY LIFECYCLE ===")
print()

for r in report:

    print(
        r["entry_pattern"],
        "| state:", r["state"],
        "| trades:", r["trades"],
        "| wins:", r["wins"]
    )

print()