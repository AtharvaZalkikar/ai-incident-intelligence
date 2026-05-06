from app.database import SessionLocal
from app.models.log import Log

from datetime import timedelta

THRESHOLD_MINUTES = 15


def get_incidents():
    db = SessionLocal()

    logs = db.query(Log).order_by(Log.timestamp).all()

    incidents = []
    current_incident = []

    for log in logs:
        # First log starts an incident
        if not current_incident:
            current_incident.append(log)
            continue

        last_log = current_incident[-1]

        time_diff = log.timestamp - last_log.timestamp

        # Same incident
        if (
            time_diff <= timedelta(minutes=THRESHOLD_MINUTES)
            and log.node_id == last_log.node_id
        ):
            current_incident.append(log)
        else:
            # Close previous incident
            incidents.append(current_incident)
            current_incident = [log]

    # Add last incident
    if current_incident:
        incidents.append(current_incident)

    db.close()

    return incidents