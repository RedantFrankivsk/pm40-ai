import difflib


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_similar(description, patterns, threshold=0.65):
    best_pid = None
    best_score = 0.0

    for pid, p in patterns.items():
        score = similarity(description, p.get("description", ""))
        if score > best_score and score >= threshold:
            best_score = score
            best_pid = pid

    return best_pid, round(best_score, 2)
