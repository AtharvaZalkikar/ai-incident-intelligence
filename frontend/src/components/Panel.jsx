export default function Panel({ title, children }) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6 shadow-sm">

      <h2 className="mb-4 text-xl font-semibold">
        {title}
      </h2>

      {children}

    </div>
  );
}