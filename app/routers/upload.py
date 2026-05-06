from fastapi import APIRouter, UploadFile, File
import csv
from io import StringIO
from datetime import datetime

from app.database import SessionLocal
from app.models.log import Log

router = APIRouter()

@router.post("/upload")
async def upload_logs(file: UploadFile = File(...)):
    db = SessionLocal()

    content = await file.read()
    csv_data = StringIO(content.decode("utf-8"))
    reader = csv.DictReader(csv_data)

    count = 0

    try:
        for row in reader:
            log = Log(
                timestamp=datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M"),
                node_id=row["node_id"],
                alarm_type=row["alarm_type"],
                severity=row["severity"],
                region=row["region"],
                failure_reason=row["failure_reason"]
            )
            db.add(log)
            count += 1

        db.commit()

        return {"message": f"{count} logs inserted"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()