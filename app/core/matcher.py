import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_best_match(embedding: np.ndarray, db_embeddings: list[np.ndarray], threshold: float = 0.5):
    """
    Cari embedding database yang paling mirip dengan input.
    """
    if len(db_embeddings) == 0:
        return None, None

    # Reshape jika perlu
    embedding = embedding.reshape(1, -1)
    db_embeddings = [e.reshape(1, -1) for e in db_embeddings]
    db_matrix = np.vstack(db_embeddings)  # Shape: (N, 512)

    similarities = cosine_similarity(embedding, db_matrix)  # Shape: (1, N)
    best_idx = np.argmax(similarities)
    best_score = similarities[0][best_idx]

    if best_score >= threshold:
        return best_idx, float(best_score)
    return None, None