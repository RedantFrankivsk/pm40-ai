import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


class PDFBrain:

    def __init__(self):

        print("Завантаження локальної моделі...")

        self.model = SentenceTransformer("models/miniLM")

        with open("knowledge.pkl", "rb") as f:
            data = pickle.load(f)

        self.patterns = data["patterns"]
        self.embeddings = np.array(data["embeddings"])


    def analyze(self, description):

        query_embedding = self.model.encode([description])[0]

        similarities = np.dot(self.embeddings, query_embedding)

        best_index = np.argmax(similarities)

        best_pattern = self.patterns[best_index]

        strength = similarities[best_index]

        signal = "NEUTRAL"

        if "uptrend" in best_pattern:
            signal = "LONG"

        if "downtrend" in best_pattern:
            signal = "SHORT"

        return signal, strength