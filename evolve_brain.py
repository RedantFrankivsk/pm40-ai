from strategy_discovery_engine import StrategyDiscoveryEngine
from anti_overfitting_engine import AntiOverfittingEngine
from strategy_mutator_engine import StrategyMutatorEngine
from mutation_experiment_engine import MutationExperimentEngine
from mutation_selection_engine import MutationSelectionEngine
from brain_evolution_engine import BrainEvolutionEngine
from genetic_evolution_engine import GeneticEvolutionEngine


print()
print("=== PM40 AUTONOMOUS EVOLUTION ===")
print()


# 1 DISCOVERY
print("STEP 1: Strategy discovery")

discovery = StrategyDiscoveryEngine()
discovered = discovery.run()

print("discovered:", len(discovered))


# 2 ANTI OVERFITTING
print()
print("STEP 2: Anti-overfitting")

ao = AntiOverfittingEngine()
filtered = ao.run()

print("filtered:", len(filtered))


# 3 MUTATION
print()
print("STEP 3: Strategy mutation")

mutator = StrategyMutatorEngine()
mutations = mutator.run()

print("mutations:", len(mutations))


# 4 MUTATION EXPERIMENTS
print()
print("STEP 4: Mutation experiments")

experiment = MutationExperimentEngine()
experiments = experiment.run()

print("tested:", len(experiments))


# 5 SELECTION
print()
print("STEP 5: Mutation selection")

selection = MutationSelectionEngine()
selected = selection.run()

print("selected:", len(selected))


# 6 BRAIN EVOLUTION
print()
print("STEP 6: Brain evolution")

brain_engine = BrainEvolutionEngine()
brains = brain_engine.evolve()

print("new brains:", len(brains))


# 7 GENETIC EVOLUTION
print()
print("STEP 7: Genetic evolution")

genetic = GeneticEvolutionEngine()
genetic_brains = genetic.evolve()

print("genetic brains:", len(genetic_brains))


print()
print("=== EVOLUTION COMPLETE ===")
print()