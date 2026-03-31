from strategy_selection_engine import StrategySelectionEngine

engine = StrategySelectionEngine()

strategies = engine.select()

print()
print("=== SELECTED STRATEGIES ===")
print()

for s in strategies:

    print(
        s["entry_pattern"],
        "| direction:", s["direction"],
        "| risk:", s["risk_model"],
        "| trades:", s["trades"],
        "| winrate:", round(s["winrate"], 3),
        "| fitness:", round(s["fitness"], 3)
    )

print()