import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

with open("knowledge.pkl", "rb") as f:
    data = pickle.load(f)

texts = data["texts"]
embeddings = data["embeddings"]

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "short term trend continuation after pullback on 1 minute chart"

query_vec = model.encode([query])[0]

scores = np.dot(embeddings, query_vec)

top_idx = scores.argsort()[-5:][::-1]

print("🔍 Найбільш релевантні фрагменти:\n")
for i in top_idx:
    print("-", texts[i][:200], "\n")
