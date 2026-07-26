from app.services.incident_service import get_incident_by_id
from app.services.llm_service import generate_completion


def format_failure_analysis(failure_analysis):
    """
    Convert structured failure analysis into readable text for the LLM.
    """

    lines = []

    for item in failure_analysis:
        lines.append(
            f"- {item['reason']}: "
            f"{item['count']} logs "
            f"({item['percentage']}%)"
        )

    return "\n".join(lines)


def investigate_incident(question: str, incident_id: int | None):

    if incident_id is None:
        return "No incident selected."

    incident = get_incident_by_id(incident_id)

    if incident is None:
        return "Incident not found."

    failure_text = format_failure_analysis(
        incident["failure_analysis"]
    )

    prompt = f"""
You are an experienced Site Reliability Engineer helping another engineer investigate an incident.

Your task is to answer the user's question using ONLY the incident information below.

If the requested information is unavailable, respond with:
"I don't have enough information to determine that."

=========================
INCIDENT DETAILS
=========================

Nodes:
{", ".join(incident["nodes"])}

Start Time:
{incident["start_time"]}

End Time:
{incident["end_time"]}

Log Count:
{incident["log_count"]}

Failure Analysis:
{failure_text}

Previous Automated Analysis:
{incident["summary"]}

=========================
USER QUESTION
=========================

{question}

=========================
RESPONSE GUIDELINES
=========================

- Answer only from the provided incident.
- Do not invent or assume facts.
- Keep the response concise (3–6 sentences).
- Explain technical concepts in simple language.
- Mention the most likely cause when possible.
- If appropriate, recommend the next troubleshooting step.
"""

    return generate_completion(prompt)