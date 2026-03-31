from pattern_memory import PatternMemory
from pattern_cluster_engine import PatternClusterEngine
from pattern_score_engine import PatternScoreEngine


memory = PatternMemory()
cluster_engine = PatternClusterEngine()
score_engine = PatternScoreEngine()


patterns = memory.get_all_patterns()


for desc, stats in patterns.items():

    trades = stats["trades"]
    wins = stats["wins"]

    cluster_engine.register(desc, trades, wins)


clusters = cluster_engine.get_clusters()


print("\n=== PATTERN CLUSTERS ===\n")


for c in clusters:

    trades = c["trades"]
    wins = c["wins"]
    winrate = c["winrate"]

    score = score_engine.calculate(trades, wins)

    print(
        c["cluster"],
        "| trades:", trades,
        "| winrate:", winrate,
        "| score:", score
    )