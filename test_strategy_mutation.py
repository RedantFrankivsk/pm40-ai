from strategy_mutation_engine import StrategyMutationEngine

engine = StrategyMutationEngine()

mutations = engine.run()

print()
print("=== STRATEGY MUTATIONS ===")
print()

for m in mutations:

    print(
        "pattern:", m["entry_pattern"],
        "| direction:", m["direction"],
        "| risk:", m["risk_model"]
    )

print()
print("Total mutations:", len(mutations))
print()