from strategy_auto_evolution_engine import StrategyAutoEvolutionEngine

engine = StrategyAutoEvolutionEngine()

strategies = engine.evolve()

print()
print("=== AUTO EVOLVED STRATEGIES ===")
print()

for s in strategies:

    print(
        s["pattern"],
        "| trades:", s["trades"],
        "| winrate:", s["winrate"],
        "| score:", s["score"]
    )

engine.save(strategies)

print()
print("Saved to auto_strategies.json")
print()