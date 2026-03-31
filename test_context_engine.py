# test_context_engine.py

from context_engine import detect_volatility
from context_engine import detect_session
from context_engine import detect_trend_strength


atr = 0.0012
price = 1.1000
hour = 9
trend_score = 2


print("\n=== CONTEXT ===\n")

print("volatility:", detect_volatility(atr, price))
print("session:", detect_session(hour))
print("trend_strength:", detect_trend_strength(trend_score))