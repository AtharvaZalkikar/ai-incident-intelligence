from fastapi import APIRouter

from app.services.incident_service import get_saved_incidents

router = APIRouter()

@router.get("/incidents")
def fetch_incidents():

    incidents = get_saved_incidents()

    return {
        "total_incidents": len(incidents),
        "incidents": incidents,
    }