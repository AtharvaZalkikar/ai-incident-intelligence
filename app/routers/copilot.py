from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CopilotRequest(BaseModel):
    question: str
    incident_id: int | None = None


@router.post("/copilot")
def investigate(request: CopilotRequest):

    return {
        "answer": f"Investigation received.\n\nQuestion: {request.question}\n\n(This is a placeholder response.)"
    }