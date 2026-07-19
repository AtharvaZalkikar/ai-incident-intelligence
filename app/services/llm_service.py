from openai import OpenAI
import os

from app.services.embedding_service import get_embedding
from app.services.similarity_service import get_similar_incidents


stored_incidents = []
stored_embeddings = []

def generate_summary(incident_data):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Convert to text
    incident_text = incident_to_text(incident_data)

    # Get embedding
    embedding = get_embedding(incident_text)

    # Retrieve similar incidents
    # similar = get_similar_incidents(embedding)
    similar = get_similar_incidents(embedding, stored_embeddings, stored_incidents)

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




def incident_to_text(incident_data):
    text = f"Nodes: {incident_data['nodes']}, Duration: {incident_data['duration']}, Reasons: "

    for r in incident_data["failure_analysis"]:
        text += f"{r['reason']} ({r['percentage']}%), "

    return text