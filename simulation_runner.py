import random

from multi_tf_builder import MultiTFBuilder
from pdf_brain import PDFBrain
from decision_engine import DecisionEngine
from pattern_memory import PatternMemory
from pattern_filter import PatternFilter


builder = MultiTFBuilder()
brain = PDFBrain()
engine = DecisionEngine()
memory = PatternMemory()
filter = PatternFilter()


wins = 0
losses = 0
neutral = 0
real_trades = 0


def generate_market():

    prices = [100]

    for i in range(60):
        prices.append(prices[-1] + random.uniform(-1, 1))

    volumes = [random.uniform(100, 200) for _ in range(60)]

    prices5 = prices[-20:]
    prices10 = prices[-40:]
    prices15 = prices

    return prices5, prices10, prices15, volumes


for i in range(400):

    prices5, prices10, prices15, volumes = generate_market()

    description = builder.build(prices5, prices10, prices15, volumes)

    signal, strength = brain.analyze(description)

    bias = memory.get_bias(description)

    decision = engine.make_decision(signal, strength, bias)

    if decision == "NEUTRAL":
        neutral += 1
        continue

    real_trades += 1

    outcome = random.choice(["WIN", "LOSS"])

    memory.update(description, outcome)

    filter.update(description, outcome)

    if outcome == "WIN":
        wins += 1
    else:
        losses += 1


print("\n=== FINAL STATS ===")

print("REAL TRADES:", real_trades)
print("WINS:", wins)
print("LOSSES:", losses)

if real_trades > 0:
    print("WINRATE:", round(wins / real_trades * 100, 2), "%")

print("NEUTRAL:", neutral)