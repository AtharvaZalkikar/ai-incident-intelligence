import Panel from "./Panel";
import EmptyState from "./EmptyState";

export default function Workspace({
    incidents,
    selectedIncident,
    onSelectIncident,
}) {

  console.log(incidents);   // <-- HERE

  return (
    <div className="mx-auto mt-8 max-w-7xl px-8">

      <div className="grid grid-cols-12 gap-6">

        <div className="col-span-4">

          <Panel title="Case Files">

              <div className="space-y-3 h-112.5 overflow-y-auto">

                  {incidents.length === 0 ? (

                      <EmptyState
                          title="No investigations yet"
                          description="Upload a log file to begin."
                      />

                  ) : (

                      incidents.map((incident, index) => (

                          <div
                              key={index}
                              onClick={() => onSelectIncident(incident)}
                              className={`cursor-pointer rounded-lg border p-4 transition ${
                                  selectedIncident === incident
                                      ? "border-cyan-400 bg-slate-700"
                                      : "border-slate-700 bg-slate-800 hover:border-cyan-400 hover:bg-slate-700"
                              }`}
                          >

                              <h3 className="font-semibold text-white">
                                  {incident.nodes.join(", ")}
                              </h3>

                              <p className="mt-1 text-sm text-slate-400">
                                  {incident.log_count} Logs
                              </p>

                              <p className="mt-2 text-xs text-slate-500">
                                  {incident.start_time}
                              </p>

                          </div>

                      ))

                  )}

              </div>

          </Panel>
        </div>

        <div className="col-span-8">

          <Panel title="Investigation">

              {selectedIncident ? (

                  <div className="space-y-6">

                      <div>

                          <h2 className="text-2xl font-bold">
                              {selectedIncident.nodes.join(", ")}
                          </h2>

                          <p className="mt-1 text-slate-400">
                              {selectedIncident.log_count} Logs
                          </p>

                      </div>

                      <div>

                          <h3 className="mb-2 text-lg font-semibold">
                              AI Summary
                          </h3>

                          <div className="rounded-lg border border-slate-700 bg-slate-800 p-4">

                              <p className="leading-7 text-slate-300">
                                  {selectedIncident.summary}
                              </p>

                          </div>

                      </div>

                  </div>

              ) : (

                  <EmptyState
                      title="No case selected"
                      description="Choose an incident from the left."
                  />

              )}

          </Panel>

        </div>

      </div>

    </div>
  );
}