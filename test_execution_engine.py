from strategy_execution_engine import StrategyExecutionEngine


engine = StrategyExecutionEngine()


test_pattern = "5m_uptrend 10m_uptrend 15m_uptrend pullback normal_volume trend_market"

should_trade = engine.should_trade(test_pattern)

print("\nPattern:", test_pattern)
print("Should trade:", should_trade)


info = engine.explain(test_pattern)

if info:
    print("Matched strategy:", info["matched_strategy"])
    print("Winrate:", info["winrate"])
    print("Score:", info["score"])