from openai import OpenAI
import os
import math

stored_incidents = []
stored_embeddings = []

def generate_summary(incident_data):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Convert to text
    incident_text = incident_to_text(incident_data)

    # Get embedding
    embedding = get_embedding(incident_text)

    # Retrieve similar incidents
    similar = get_similar_incidents(embedding)

    # Build context
    similar_text = "\n".join([incident_to_text(s) for s in similar])

    prompt = f"""
        You are a site reliability engineer.

        Analyze the incident using ONLY the provided data.

        STRICT RULES:
        - DO NOT invent or assume any incidents
        - ONLY use the "Similar Past Incidents" section
        - If no similar incidents are provided, say: "No similar incidents found"
        - Keep answer concise (2-4 lines max)
        - Clearly mention primary cause

        Current Incident:
        {incident_text}

        Similar Past Incidents:
        {similar_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Store this incident for future use
    stored_incidents.append(incident_data)
    stored_embeddings.append(embedding)

    return response.choices[0].message.content


def get_embedding(text):
    from openai import OpenAI
    import os

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

def incident_to_text(incident_data):
    text = f"Nodes: {incident_data['nodes']}, Duration: {incident_data['duration']}, Reasons: "

    for r in incident_data["failure_analysis"]:
        text += f"{r['reason']} ({r['percentage']}%), "

    return text


def cosine_similarity(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x*x for x in a))
    norm_b = math.sqrt(sum(x*x for x in b))
    return dot / (norm_a * norm_b)


def get_similar_incidents(query_embedding, top_k=2):
    similarities = []

    for i, emb in enumerate(stored_embeddings):
        sim = cosine_similarity(query_embedding, emb)
        similarities.append((sim, stored_incidents[i]))

    similarities.sort(reverse=True, key=lambda x: x[0])

    return [item[1] for item in similarities[:top_k]]