import api from "./api";

export async function askCopilot(question, incidentId) {
    const response = await api.post("/copilot", {
        question: question,
        incident_id: incidentId,
    });

    return response.data;
}