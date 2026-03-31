from edge_reinforcement_engine import EdgeReinforcementEngine

engine = EdgeReinforcementEngine()

patterns = engine.pattern_reinforcement()

print()
print("=== EDGE REINFORCEMENT ===")
print()

for p in patterns:

    print(
        p["pattern"],
        "| trades:", p["trades"],
        "| wins:", p["wins"],
        "| winrate:", round(p["winrate"], 3),
        "| strength:", round(p["strength"], 3)
    )

print()

strongest = engine.strongest_patterns()

print("=== STRONGEST PATTERNS ===")
print()

for s in strongest:

    print(
        s["pattern"],
        "| strength:", round(s["strength"], 3)
    )

print()