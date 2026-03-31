import json
import os
import random


class DiscoveryEngine:

    def __init__(self):

        self.pattern_file = "pattern_memory_storage.json"

    def load_patterns(self):

        if not os.path.exists(self.pattern_file):
            return {}

        with open(self.pattern_file, "r") as f:
            return json.load(f)

    def extract_tokens(self):

        patterns = self.load_patterns()

        tokens = set()

        for pattern in patterns:

            parts = pattern.split()

            for p in parts:
                tokens.add(p)

        return list(tokens)

    def generate_patterns(self, count=5):

        tokens = self.extract_tokens()

        if len(tokens) < 2:
            return []

        new_patterns = []

        for _ in range(count):

            size = random.randint(2, 3)

            parts = random.sample(tokens, min(size, len(tokens)))

            pattern = " ".join(parts)

            new_patterns.append(pattern)

        return new_patterns