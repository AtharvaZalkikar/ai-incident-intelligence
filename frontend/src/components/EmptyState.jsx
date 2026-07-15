export default function EmptyState({ title, description }) {
  return (
    <div className="flex h-[450px] items-center justify-center rounded-lg border border-dashed border-slate-700">

      <div className="text-center">

        <h3 className="text-xl font-semibold">
          {title}
        </h3>

        <p className="mt-2 text-slate-500">
          {description}
        </p>

      </div>

    </div>
  );
}