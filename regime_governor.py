# decision_engine.py

from pattern_memory import memory
from regime_governor import regime_governor
import hashlib


def _make_pid(description: str, session: str):
    return hashlib.sha256(f"{description}|{session}".encode()).hexdigest()


def get_signal(
    description: str,
    base_signal: str,
    base_confidence: float,
    regime: str,
    session: str
):
    print("[ENGINE] get_signal called")

    pid = _make_pid(description, session)
    p = memory.get_or_create(pid)

    confidence = base_confidence
    risk = 0.16 * confidence

    notes = []

    # === Regime Governor ===
    gov = regime_governor(regime)
    confidence *= gov["confidence_mult"]
    risk *= gov["risk_mult"]
    notes.extend(gov["notes"])

    if gov["force_neutral"]:
        signal = "NEUTRAL"
        notes.append("Governor forced NEUTRAL")
    else:
        signal = base_signal

    engine = {
        "pid": pid,
        "signal": signal,
        "raw_confidence": base_confidence,
        "confidence": round(confidence, 3),
        "strength": "MEDIUM" if confidence >= 0.7 else "WEAK",
        "authority": p["authority"],
        "psi": p["psi"],
        "streak": p["streak"],
        "trusted": p["trusted"],
        "locked": p["locked"],
        "cooldown": p["cooldown"],
        "pattern_quality": p["quality"],
        "confidence_decay": p["confidence_decay"],
        "fatigue": p["fatigue"],
        "suppression": p["suppression"],
        "trust_lock": p.get("trust_lock"),
        "generation": p.get("generation", 0),
        "parent_pid": p.get("parent_pid"),
        "mutation_score": p.get("mutation_score", 0.0),
        "regime": regime,
        "session": session,
        "risk": round(risk, 3),
        "notes": notes
    }

    return engine


def evaluate(engine: dict):
    print("[ENGINE] evaluate called")

    meta = {
        "allow_trade": engine["signal"] != "NEUTRAL",
        "reason": "OK" if engine["signal"] != "NEUTRAL" else "Forced neutral",
        "adjusted_risk": engine["risk"],
        "meta_score": 1.0,
        "notes": engine["notes"]
    }

    return meta


def register_trade_result(pid: str, result: str):
    print(f"[ENGINE] register_trade_result {pid} {result}")
    memory.register_result(pid, result)
