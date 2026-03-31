from pattern_mutation_engine import PatternMutationEngine


engine = PatternMutationEngine()


base_pattern = "normal_volume pullback trend_market"


mutations = engine.mutate(base_pattern, 10)


print("\nBase pattern:")
print(base_pattern)

print("\nMutations:\n")

for m in mutations:
    print(m)