class PatternClusterEngine:

    def __init__(self):
        self.clusters = {}

    def simplify(self, description):

        parts = description.split()

        normalized = []

        for p in parts:

            # прибираємо multi-timeframe тренди
            if p.startswith("5m_") or p.startswith("10m_") or p.startswith("15m_"):
                continue

            # прибираємо конкретний напрям тренду
            if p == "uptrend" or p == "downtrend":
                continue

            normalized.append(p)

        # прибираємо дублікати
        normalized = sorted(set(normalized))

        key = " ".join(normalized)

        return key

    def register(self, description, trades, wins):

        key = self.simplify(description)

        if key not in self.clusters:

            self.clusters[key] = {
                "trades": 0,
                "wins": 0
            }

        self.clusters[key]["trades"] += trades
        self.clusters[key]["wins"] += wins

    def get_clusters(self, min_trades=40):

        results = []

        for k, v in self.clusters.items():

            trades = v["trades"]
            wins = v["wins"]

            if trades < min_trades:
                continue

            winrate = wins / trades

            results.append({
                "cluster": k,
                "trades": trades,
                "wins": wins,
                "winrate": round(winrate, 3)
            })

        return results