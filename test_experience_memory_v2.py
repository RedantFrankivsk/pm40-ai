from experience_memory_engine import ExperienceMemoryEngine

engine = ExperienceMemoryEngine()

pattern = [
    "normal_volume",
    "pullback",
    "trend_market"
]

context = [
    "session_london",
    "volatility_normal",
    "strong_trend"
]

strategy = {
    "pattern": "pullback trend_market",
    "direction": "reversal",
    "risk": "adaptive"
}

engine.record_experience(
    signal="DOWN",
    pattern_tokens=pattern,
    context_tokens=context,
    regime="trend_market",
    strategy=strategy,
    confidence=0.84,
    result="WIN"
)

engine.record_experience(
    signal="DOWN",
    pattern_tokens=pattern,
    context_tokens=context,
    regime="trend_market",
    strategy=strategy,
    confidence=0.40,
    result="LOSS"
)

stats = engine.stats()

print()
print("=== EXPERIENCE MEMORY V2 ===")
print()

print("Total trades:", stats["total"])
print("Wins:", stats["wins"])
print("Losses:", stats["losses"])
print("Winrate:", round(stats["winrate"], 3))

print()