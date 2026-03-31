from strategy_mutator_engine import StrategyMutatorEngine


engine = StrategyMutatorEngine()

mutations = engine.mutate()

print()
print("=== PM40 STRATEGY MUTATIONS ===")
print()

for m in mutations:

    print(m["pattern"], "| parent:", m["parent"])