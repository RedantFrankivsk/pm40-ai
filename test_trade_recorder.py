from trade_recorder import TradeRecorder

recorder = TradeRecorder()

pattern = "normal_volume pullback trend_market session_london volatility_normal strong_trend"

recorder.record(pattern, "WIN")
recorder.record(pattern, "LOSS")
recorder.record(pattern, "WIN")