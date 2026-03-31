import json
import os

STATS_FILE = "stats.json"

DEFAULT_STATS = {
    "global": {
        "wins": 0,
        "losses": 0,
        "loss_streak": 0,
        "cooldown": 0
    },
    "by_signal": {
        "UP": {"wins": 0, "losses": 0},
        "DOWN": {"wins": 0, "losses": 0},
        "NEUTRAL": {"skips": 0}
    },
    "by_tf": {}
}


def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)


def load_stats():
    if not os.path.exists(STATS_FILE):
        save_stats(DEFAULT_STATS)

    with open(STATS_FILE, "r", encoding="utf-8") as f:
        stats = json.load(f)

    # ===== BACKWARD COMPATIBILITY =====
    stats.setdefault("global", {})
    stats["global"].setdefault("wins", 0)
    stats["global"].setdefault("losses", 0)
    stats["global"].setdefault("loss_streak", 0)
    stats["global"].setdefault("cooldown", 0)

    stats.setdefault("by_signal", {
        "UP": {"wins": 0, "losses": 0},
        "DOWN": {"wins": 0, "losses": 0},
        "NEUTRAL": {"skips": 0}
    })

    stats.setdefault("by_tf", {})

    save_stats(stats)
    return stats


def _winrate(w, l):
    total = w + l
    return round(w / total * 100, 2) if total > 0 else 50


def register_result(signal, tf, result):
    stats = load_stats()

    if tf not in stats["by_tf"]:
        stats["by_tf"][tf] = {"wins": 0, "losses": 0}

    # === NEUTRAL ===
    if signal == "NEUTRAL":
        stats["by_signal"]["NEUTRAL"]["skips"] += 1
        save_stats(stats)
        return stats

    if result == "win":
        stats["global"]["wins"] += 1
        stats["global"]["loss_streak"] = 0
        stats["by_signal"][signal]["wins"] += 1
        stats["by_tf"][tf]["wins"] += 1

    elif result == "loss":
        stats["global"]["losses"] += 1
        stats["global"]["loss_streak"] += 1
        stats["by_signal"][signal]["losses"] += 1
        stats["by_tf"][tf]["losses"] += 1

    # === COOLDOWN LOGIC ===
    ls = stats["global"]["loss_streak"]

    if ls >= 5:
        stats["global"]["cooldown"] = 2
    elif ls >= 3:
        stats["global"]["cooldown"] = 1
    else:
        stats["global"]["cooldown"] = 0

    save_stats(stats)
    return stats


def get_tf_winrate(tf):
    stats = load_stats()
    tfstat = stats["by_tf"].get(tf)
    if not tfstat:
        return 50
    return _winrate(tfstat["wins"], tfstat["losses"])


def get_signal_winrate(signal):
    stats = load_stats()
    s = stats["by_signal"].get(signal)
    if not s:
        return 50
    return _winrate(s.get("wins", 0), s.get("losses", 0))
