import { Activity } from "lucide-react";

export default function Header() {
  return (
    <header className="border-b border-slate-800">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">

        <div className="flex items-center gap-3">

          <Activity className="text-cyan-400" size={28} />

          <div>
            <h1 className="text-xl font-bold">
              AI Incident Intelligence
            </h1>

            <p className="text-sm text-slate-400">
              Investigation Workspace
            </p>
          </div>

        </div>

        <div className="flex items-center gap-2">

          <div className="h-2 w-2 rounded-full bg-green-500" />

          <span className="text-sm text-slate-400">
            Backend Ready
          </span>

        </div>

      </div>
    </header>
  );
}