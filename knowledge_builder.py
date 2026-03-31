import pickle
from sentence_transformers import SentenceTransformer


print("Завантаження моделі...")

model = SentenceTransformer("models/miniLM")


patterns = [

"uptrend impulse high_volume trend_market",
"uptrend impulse normal_volume trend_market",
"uptrend pullback low_volume trend_market",

"downtrend impulse high_volume trend_market",
"downtrend impulse normal_volume trend_market",
"downtrend pullback low_volume trend_market",

"sideways range normal_volume range_market",
"sideways range low_volume range_market",

"uptrend impulse high_volume volatile_market",
"downtrend impulse high_volume volatile_market"

]


embeddings = model.encode(patterns)


data = {
    "patterns": patterns,
    "embeddings": embeddings
}


with open("knowledge.pkl", "wb") as f:
    pickle.dump(data, f)


print("Knowledge base створена")
print("Патернів:", len(patterns))