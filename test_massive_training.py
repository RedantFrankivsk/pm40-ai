from massive_training_loop import MassiveTrainingLoop

engine = MassiveTrainingLoop()

report = engine.run(
    cycles=5,
    trades_per_cycle=50
)

print()
print("=== PM40 MASSIVE TRAINING ===")
print()

print("TOTAL TRADES:", report["total_trades"])
print("WINS:", report["wins"])
print("WINRATE:", report["winrate"])

print()
print("BRAIN WEIGHTS:")

for k, v in report["brain_weights"].items():
    print(k, ":", v)

print()
print("BRAIN REPORT:")
print(report["brain_report"])
print()