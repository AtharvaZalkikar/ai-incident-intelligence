import { useState } from "react";


export default function CopilotPanel() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    return (
        <div className="space-y-4">

            <h3 className="text-lg font-semibold">
                AI Investigator
            </h3>

            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask about this incident..."
                className="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white placeholder:text-slate-500 focus:border-cyan-400 focus:outline-none"
            />

            <button
                className="rounded-lg bg-cyan-500 px-5 py-2 font-medium text-slate-900 transition hover:bg-cyan-400"
                onClick={() => setAnswer(question)}
            >
                Investigate
            </button>

            <div>

                <p className="mb-2 text-sm text-slate-400">
                    Suggested Questions
                </p>

                <div className="flex flex-wrap gap-2">

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400">
                        Why did this happen?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400">
                        Is this recurring?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400">
                        Root cause?
                    </button>

                    <button className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-cyan-400">
                        Explain simply
                    </button>

                </div>

            </div>

            <div className="rounded-lg border border-dashed border-slate-700 p-4 text-slate-500">

                {answer || "Investigation results will appear here."}

            </div>

        </div>
    );
}