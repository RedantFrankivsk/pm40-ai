from strategy_generator import StrategyGenerator


class StrategyExecutionEngine:

    def __init__(self):

        generator = StrategyGenerator()
        self.strategies = generator.build()

        print(f"[GENERATOR] Built {len(self.strategies)} strategies")

        self.strategy_tokens = []

        for s in self.strategies:

            raw_tokens = set()

            if "pattern" in s:
                raw_tokens = set(s["pattern"].replace("|", "").split())

            elif "type" in s:
                raw_tokens = set(s["type"].split("_"))

            tokens = self.normalize_tokens(raw_tokens)

            self.strategy_tokens.append({
                "tokens": tokens,
                "data": s
            })

    def normalize_tokens(self, tokens):

        normalized = set()

        for t in tokens:
            t = t.lower()

            if "_" in t:
                parts = t.split("_")
                normalized.update(parts)
            else:
                normalized.add(t)

        return normalized

    def match_score(self, pattern_tokens, strategy_tokens):

        if not strategy_tokens:
            return 0

        common = pattern_tokens.intersection(strategy_tokens)

        score = len(common) / len(strategy_tokens)

        if "up" in common or "down" in common:
            score += 0.1

        return min(score, 1.0)

    def should_trade(self, pattern_description):

        raw_tokens = set(pattern_description.replace("|", "").split())
        pattern_tokens = self.normalize_tokens(raw_tokens)

        best_score = 0
        best_strategy = None

        for s in self.strategy_tokens:

            score = self.match_score(pattern_tokens, s["tokens"])

            if score > best_score:
                best_score = score
                best_strategy = s

        weight = 1
        if best_strategy:
            weight = best_strategy["data"].get("weight", 1)

        final_score = best_score * weight

        print(f"[EXECUTION] best_score={round(best_score,2)} weight={weight} final={round(final_score,2)}")

        # 🔥 МІНІ ФІКС — трохи впливу
        if final_score < 0.2:
            print("[PIPELINE] ⚠️ VERY WEAK → still allow (learning)")
            return True

        if final_score < 0.5:
            print(f"[PIPELINE] ⚠️ MEDIUM ({round(final_score,2)})")
            return True

        print(f"[PIPELINE] ✅ STRONG ({round(final_score,2)})")
        return True