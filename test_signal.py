from decision_engine import get_signal, evaluate, register_trade_result

print("=== TEST SIGNAL START ===")

engine = get_signal(
    description="нисходящий тренд, откат вверх, объем падает",
    base_signal="DOWN",
    regime="TREND",
    session="LONDON"
)

meta = evaluate(engine)

print("\nENGINE:")
for k, v in engine.items():
    print(f"  {k}: {v}")

print("\nMETA:")
for k, v in meta.items():
    print(f"  {k}: {v}")

if meta["execute"]:
    result = "WIN"
    print("\nRESULT:", result)
    register_trade_result(engine, result)
else:
    print("\nNO TRADE EXECUTED")

print("=== TEST SIGNAL END ===")
