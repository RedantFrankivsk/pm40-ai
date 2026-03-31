from brain_ranking_engine import BrainRankingEngine

print()
print("=== PM40 BRAIN RANKING ===")
print()

engine = BrainRankingEngine()

brains = engine.run()

for b in brains:

    print(
        b["name"],
        "| forward:", b["forward_winrate"],
        "| experiment:", b["experiment_winrate"],
        "| score:", b["score"]
    )