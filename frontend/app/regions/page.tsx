export default function RegionsPage() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-black text-slate-900">المناطق</h1>
      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded-2xl bg-white p-5 shadow-soft">الرياض</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">الشرق</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">منطقة مكة</div>
      </div>
    </main>
  );
}
