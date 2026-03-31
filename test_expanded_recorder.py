from expanded_trade_recorder import ExpandedTradeRecorder

recorder = ExpandedTradeRecorder()

pattern = "normal_volume pullback trend_market session_london volatility_normal strong_trend"

recorder.record(pattern, "WIN")
recorder.record(pattern, "LOSS")
recorder.record(pattern, "WIN")