import itertools


class PatternExpansionEngine:

    def expand(self, pattern):

        tokens = pattern.split()

        expansions = set()

        for r in range(1, len(tokens) + 1):

            combos = itertools.combinations(tokens, r)

            for c in combos:

                expansions.add(" ".join(sorted(c)))

        return list(expansions)