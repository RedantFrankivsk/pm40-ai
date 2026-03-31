# stats_tracker.py

import json
import os

FILE_NAME = "stats.json"


def load_stats():
    if not os.path.exists(FILE_NAME):
        return {"wins": 0, "losses": 0}

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_stats(stats):
    with open(FILE_NAME, "w") as f:
        json.dump(stats, f, indent=2)


def update_stats(closed_trades):
    stats = load_stats()

    for t in closed_trades:
        if t["result"] > 0:
            stats["wins"] += 1
        else:
            stats["losses"] += 1

    save_stats(stats)


def print_stats():
    stats = load_stats()
    total = stats["wins"] + stats["losses"]

    if total == 0:
        print("📊 No trades yet")
        return

    winrate = stats["wins"] / total * 100

    print(f"\n📊 STATS:")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Winrate: {winrate:.2f}%\n")