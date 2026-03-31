from strategy_auto_evolution_engine import StrategyAutoEvolutionEngine

engine = StrategyAutoEvolutionEngine()

strategies = engine.evolve()

print()
print("=== TEST AUTO EVOLUTION ===")
print()

for s in strategies:
    print(s)