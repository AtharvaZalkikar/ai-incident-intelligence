from fastapi import APIRouter
from app.database import SessionLocal
from app.models.log import Log

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "API is running"}



@router.get("/check-db")
def check_db():
    db = SessionLocal()
    try:
        logs = db.query(Log).all()
        return {"total_logs": len(logs)}
    finally:
        db.close()

@router.delete("/clear-logs")
def clear_logs():
    db = SessionLocal()
    try:
        db.query(Log).delete()
        db.commit()
        return {"message": "All logs deleted"}
    finally:
        db.close()