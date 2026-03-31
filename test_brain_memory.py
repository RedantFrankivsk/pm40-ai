from brain_memory import BrainMemory

print()
print("=== PM40 BRAIN MEMORY TEST ===")
print()

memory = BrainMemory()

memory.record_signal(
    "breakout_pullback_trend_market_brain",
    ["breakout","pullback","trend_market"],
    "UP"
)

memory.record_signal(
    "breakout_pullback_trend_market_brain",
    ["breakout","pullback","trend_market"],
    "DOWN"
)

memory.record_result(0, "win")
memory.record_result(1, "loss")

stats = memory.get_brain_stats("breakout_pullback_trend_market_brain")

print("wins:", stats["wins"])
print("losses:", stats["losses"])
print("winrate:", stats["winrate"])