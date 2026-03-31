from pattern_memory import PatternMemory

memory = PatternMemory()

patterns = memory.all_patterns()

print()
print("=== PATTERN MEMORY INSPECTION ===")
print()

print("Total patterns:", len(patterns))
print()

for pattern in patterns:

    stats = memory.get_pattern_stats(pattern)

    trades = stats["trades"]
    wins = stats["wins"]

    if trades == 0:
        winrate = 0
    else:
        winrate = wins / trades

    print(
        pattern,
        "| trades:", trades,
        "| wins:", wins,
        "| winrate:", round(winrate, 3)
    )

print()