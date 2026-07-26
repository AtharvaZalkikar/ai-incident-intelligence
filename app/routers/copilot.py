from fastapi import APIRouter
from pydantic import BaseModel

from app.services.copilot_service import investigate_incident

router = APIRouter()


class CopilotRequest(BaseModel):
    question: str
    incident_id: int | None = None


@router.post("/copilot")
def investigate(request: CopilotRequest):
    print(request.incident_id)

    # return {
    #     "answer": f"Investigation received.\n\nQuestion: {request.question}\n\n(This is a placeholder response.)"
    # }

    answer = investigate_incident(
        request.question,
        request.incident_id,
    )

    return {
        "answer": answer
    }