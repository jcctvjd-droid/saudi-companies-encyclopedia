export default function CitiesPage() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-black text-slate-900">المدن</h1>
      <div className="grid gap-4 md:grid-cols-4">
        <div className="rounded-2xl bg-white p-5 shadow-soft">الرياض</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">الظهران</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">جدة</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">الدمام</div>
      </div>
    </main>
  );
}
