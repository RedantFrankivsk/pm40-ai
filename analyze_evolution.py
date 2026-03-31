from pattern_memory import PatternMemory
from pattern_evolution_engine import PatternEvolutionEngine


memory = PatternMemory()
engine = PatternEvolutionEngine()


patterns = memory.get_all_patterns()


for desc, stats in patterns.items():

    trades = stats["trades"]
    wins = stats["wins"]

    for i in range(trades):

        if i < wins:
            outcome = "WIN"
        else:
            outcome = "LOSS"

        engine.register(desc, outcome)


strong = engine.get_strong_patterns()


print("\n=== DISCOVERED STRONG PATTERNS ===\n")


if not strong:
    print("No strong patterns discovered yet.")
else:

    for p in strong:

        print(
            p["pattern"],
            "| trades:", p["trades"],
            "| winrate:", p["winrate"]
        )