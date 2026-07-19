import json
from datetime import datetime, UTC

from app.database import SessionLocal
from app.models.incident import Incident
from app.services.analysis_service import get_incidents
from app.services.llm_service import generate_summary, reset_memory



def build_failure_analysis(incident):
    """
    Build failure analysis with count and percentage.
    """

    failure_count = {}

    for log in incident:
        reason = log.failure_reason
        failure_count[reason] = failure_count.get(reason, 0) + 1

    total = len(incident)

    failure_analysis = []

    for reason, count in failure_count.items():
        failure_analysis.append(
            {
                "reason": reason,
                "count": count,
                "percentage": round((count / total) * 100, 2),
            }
        )

    return failure_analysis


def refresh_incidents():
    """
    Rebuild the processed Incident table from raw logs.
    """

    db = SessionLocal()

    try:

        # Remove old processed incidents
        db.query(Incident).delete()

        reset_memory()

        incidents = get_incidents()

        for incident in incidents:

            failure_analysis = build_failure_analysis(incident)

            incident_data = {
                "nodes": list(set(log.node_id for log in incident)),
                "failure_analysis": failure_analysis,
                "duration": f"{incident[0].timestamp} to {incident[-1].timestamp}",
            }

            summary = generate_summary(incident_data)

            db.add(
                Incident(
                    start_time=incident[0].timestamp,
                    end_time=incident[-1].timestamp,
                    log_count=len(incident),
                    nodes=json.dumps(incident_data["nodes"]),
                    failure_analysis=json.dumps(failure_analysis),
                    summary=summary,
                    created_at=datetime.now(UTC),
                )
            )

        db.commit()

    finally:
        db.close()


def get_saved_incidents():
    db = SessionLocal()

    try:
        incidents = db.query(Incident).all()

        response = []

        for incident in incidents:
            response.append(
                {
                    "start_time": incident.start_time,
                    "end_time": incident.end_time,
                    "log_count": incident.log_count,
                    "nodes": json.loads(incident.nodes),
                    "failure_analysis": json.loads(incident.failure_analysis),
                    "summary": incident.summary,
                }
            )

        return response

    finally:
        db.close()