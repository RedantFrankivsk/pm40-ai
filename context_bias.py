# context_bias.py
# v9.3 — TF + Session bias model

def tf_bias(tf: str) -> float:
    tf = tf.upper()
    if tf == "M1":
        return -0.15
    if tf == "M5":
        return 0.0
    if tf == "M15":
        return 0.05
    return 0.1  # H1+

def session_bias(session: str) -> float:
    session = session.upper()
    if session == "ASIA":
        return -0.1
    if session == "LONDON":
        return 0.05
    if session == "NEW_YORK":
        return 0.1
    return 0.0

def apply_context_bias(confidence: float, tf: str, session: str) -> float:
    biased = confidence + tf_bias(tf) + session_bias(session)
    return round(max(0.0, min(1.0, biased)), 2)
