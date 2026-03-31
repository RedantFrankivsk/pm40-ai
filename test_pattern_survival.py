from pattern_survival_engine import PatternSurvivalEngine

engine = PatternSurvivalEngine()

population = engine.evaluate_population()

print()
print("=== PATTERN SURVIVAL REPORT ===")
print()

print("SURVIVORS:")
print()

for s in population["survivors"]:

    print(
        s["pattern"],
        "| trades:", s["trades"],
        "| winrate:", s["winrate"],
        "| confidence:", s["confidence"]
    )

print()
print("EXTINCT:")
print()

for e in population["extinct"]:

    print(
        e["pattern"],
        "| trades:", e["trades"],
        "| confidence:", e["confidence"]
    )

print()