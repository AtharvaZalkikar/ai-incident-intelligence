import math


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))

    if norm_a == 0 or norm_b == 0:
        return 0
    
    return dot / (norm_a * norm_b)


def get_similar_incidents(query_embedding, stored_embeddings, stored_incidents, top_k=2):
    similarities = []

    for i, embedding in enumerate(stored_embeddings):
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((similarity, stored_incidents[i]))

    similarities.sort(reverse=True, key=lambda x: x[0])

    return [incident for _, incident in similarities[:top_k]]