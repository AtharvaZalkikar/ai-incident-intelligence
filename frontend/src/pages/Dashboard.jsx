import { useEffect, useState } from "react";

import UploadBox from "../components/UploadBox";
import Workspace from "../components/Workspace";

import { getIncidents } from "../services/incidentService";

export default function Dashboard() {

    const [incidents, setIncidents] = useState([]);

    const [selectedIncident, setSelectedIncident] = useState(null);

    async function loadIncidents() {

        try {

            const data = await getIncidents();

            setIncidents(data.incidents);

        } catch (err) {

            console.error(err);

        }

    }

    useEffect(() => {

        loadIncidents();

    }, []);

    return (
        <>
            <UploadBox onUploadSuccess={loadIncidents} />

            <Workspace
                incidents={incidents}
                selectedIncident={selectedIncident}
                onSelectIncident={setSelectedIncident}
            />
        </>
    );
}