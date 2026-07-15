import api from "./api";

export async function getIncidents() {
    const response = await api.get("/incidents");
    return response.data;
}