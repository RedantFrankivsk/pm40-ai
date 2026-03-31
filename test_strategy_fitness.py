from strategy_fitness_engine import StrategyFitnessEngine

engine = StrategyFitnessEngine()

results = engine.evaluate()

print()
print("=== STRATEGY FITNESS ===")
print()

for r in results:

    print(
        r["entry_pattern"],
        "| direction:", r["direction"],
        "| risk:", r["risk_model"],
        "| trades:", r["trades"],
        "| winrate:", round(r["winrate"], 3),
        "| fitness:", round(r["fitness"], 3)
    )

print()