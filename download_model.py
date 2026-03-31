from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

print("Завантаження моделі...")

model = SentenceTransformer(MODEL_NAME)

model.save("models/miniLM")

print("Модель успішно збережена в models/miniLM")