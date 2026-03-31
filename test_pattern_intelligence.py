from pattern_intelligence_engine import PatternIntelligenceEngine

engine = PatternIntelligenceEngine()

patterns = engine.analyze()

print()
print("=== PM40 PATTERN INTELLIGENCE ===")
print()

for p in patterns[:10]:

    print(
        p["pattern"],
        "| trades:", p["trades"],
        "| wins:", p["wins"],
        "| winrate:", p["winrate"]
    )

print()