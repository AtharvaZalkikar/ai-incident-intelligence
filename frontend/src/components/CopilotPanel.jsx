import { useState } from "react";
import { askCopilot } from "../services/copilotService";

export default function CopilotPanel({ selectedIncident }) {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleInvestigate() {

        if (!question.trim()) {
            return;
        }

        try {

            setLoading(true);

            const response = await askCopilot(question, selectedIncident.id);

            setAnswer(response.answer);

        } catch (err) {

            console.error(err); 

            setAnswer("Something went wrong.");

        } finally {

            setLoading(false);

        }
    }

    async function askQuestion(text) {

        setQuestion(text);

        try {

            setLoading(true);

            const response = await askCopilot(
                text,
                selectedIncident.id
            );

            setAnswer(response.answer);

        } catch (err) {

            console.error(err);

            setAnswer("Something went wrong.");

        } finally {

            setLoading(false);

        }

    }

    return (
        <div className="space-y-4">

            <h3 className="text-lg font-semibold">
                AI Investigator
            </h3>

            <input
                type="text"
                value={question}
                // disabled={!selectedIncident}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask about this incident..."
                className="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white placeholder:text-slate-500 focus:border-cyan-400 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50"
            />

            <button
                    onClick={handleInvestigate}
                    disabled={loading || !selectedIncident}
                    className="rounded-lg bg-cyan-500 px-5 py-2 font-medium text-slate-900 transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-50"
                >
                    {loading ? "Investigating..." : "Ask AI Investigator"}
                </button>

            <div>

                <p className="mb-2 text-sm text-slate-400">
                    Suggested Questions
                </p>

                <div className="flex flex-wrap gap-2">

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400"
                        onClick={() => askQuestion("Why did this happen?")}
                    >
                        Why did this happen?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400"
                    onClick={() => askQuestion("Is this recurring?")}
                    >
                        Is this recurring?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400"
                    onClick={() => askQuestion("Root cause?")}>
                        Root cause?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400"
                    onClick={() => askQuestion("Explain simply")}>
                        Explain simply
                    </button>

                </div>

            </div>

            <div className="rounded-lg border border-cyan-900 bg-slate-800 p-5">

                <div className="mb-4 flex items-center gap-2">

                    <span className="text-2xl">
                        🤖
                    </span>

                    <h4 className="font-semibold text-cyan-300">
                        AI Investigator
                        
                    </h4>
                    
                </div>

                <hr className="my-3 border-slate-700" />

                {loading ? (

                    <p className="animate-pulse leading-7 text-cyan-300">
                        Investigating the incident...
                    </p>

                ) : answer ? (

                    <p className="whitespace-pre-line leading-7 text-slate-300">
                        {answer}
                    </p>

                ) : (

                    <p className="leading-7 text-slate-500">
                        Ask a question about this incident or choose one of the suggested prompts below.
                    </p>

                )}

            </div>

        </div>
    );
}