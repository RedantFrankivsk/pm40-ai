import PyPDF2
import os
from sentence_transformers import SentenceTransformer, util
import torch

# Завантаження всіх PDF і генерація ембедінгів
def load_pdfs(folder="pdf_books"):
    texts = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder, filename)
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        texts.append(text)
    return texts

# Генерація ембедінгів для тексту PDF
def embed_texts(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # компактна і швидка модель
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings, model

# Пошук найбільш релевантних правил
def search_rules(texts, embeddings, model, query, top_k=5):
    query_emb = model.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_emb, embeddings)[0]
    top_results = torch.topk(cos_scores, k=min(top_k, len(texts)))
    rules = [texts[idx] for idx in top_results.indices]
    return rules
