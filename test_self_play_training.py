from self_play_training_engine import SelfPlayTrainingEngine

engine = SelfPlayTrainingEngine()

trades = engine.run(20)

print()
print("=== PM40 SELF PLAY TRAINING ===")
print()

wins = 0

for t in trades:

    if t["result"] == "win":
        wins += 1

    print(
        t["signal"],
        "| regime:", t["regime"],
        "| result:", t["result"]
    )

print()
print("TOTAL TRADES:", len(trades))
print("WINS:", wins)
print("WINRATE:", round(wins / len(trades), 3))
print()