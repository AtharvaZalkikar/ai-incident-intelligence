from fastapi import APIRouter
from app.services.analysis_service import get_incidents
from app.services.llm_service import generate_summary

router = APIRouter()


@router.get("/incidents")
def fetch_incidents():
    incidents = get_incidents()

    response = []

    for incident in incidents:
        # Step 1: Count failure reasons
        failure_count = {}

        for log in incident:
            reason = log.failure_reason
            failure_count[reason] = failure_count.get(reason, 0) + 1

        # Step 2: Calculate percentage
        total = len(incident)
        failure_analysis = []

        for reason, count in failure_count.items():
            percentage = (count / total) * 100

            failure_analysis.append({
                "reason": reason,
                "count": count,
                "percentage": round(percentage, 2)
            })

        # ✅ Step 3: Build incident data AFTER loop
        incident_data = {
            "nodes": list(set(log.node_id for log in incident)),
            "failure_analysis": failure_analysis,
            "duration": f"{incident[0].timestamp} to {incident[-1].timestamp}"
        }

        # ✅ Step 4: Call LLM ONCE
        # summary = generate_summary(incident_data)
        try:
            summary = generate_summary(incident_data)
        except Exception as e:
            summary = f"LLM unavailable: {str(e)}"

        # Step 5: Build response
        response.append({
            "start_time": incident[0].timestamp,
            "end_time": incident[-1].timestamp,
            "log_count": len(incident),
            "nodes": list(set(log.node_id for log in incident)),
            "failure_analysis": failure_analysis,
            "summary": summary
        })

    return {
        "total_incidents": len(response),
        "incidents": response
    }