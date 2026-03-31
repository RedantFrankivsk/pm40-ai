from curiosity_engine import CuriosityEngine

engine = CuriosityEngine()

rare = engine.find_rare_patterns()

print()
print("=== PM40 CURIOSITY ENGINE ===")
print()

print("Rare patterns:", len(rare))

for r in rare[:10]:

    print(
        r["pattern"],
        "| trades:", r["trades"]
    )

print()