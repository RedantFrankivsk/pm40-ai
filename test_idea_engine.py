from idea_engine import IdeaEngine

engine = IdeaEngine()

experiments = engine.create_experiments_from_ideas()

print()
print("=== PM40 IDEA ENGINE ===")
print()

print("New strategy ideas:", len(experiments))
print()

for e in experiments:

    print(
        e["pattern"],
        "| direction:", e["direction"],
        "| risk:", e["risk"]
    )

print()