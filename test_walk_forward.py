from walk_forward_engine import WalkForwardEngine
import random


trades = []

for i in range(200):

    if random.random() < 0.62:
        trades.append("win")
    else:
        trades.append("loss")


engine = WalkForwardEngine()

result = engine.validate(trades)

print()
print("=== PM40 WALK FORWARD TEST ===")
print()

for k, v in result.items():
    print(k, ":", v)