export default function SectorsPage() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-black text-slate-900">القطاعات</h1>
      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded-2xl bg-white p-5 shadow-soft">الاتصالات</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">النفط والغاز</div>
        <div className="rounded-2xl bg-white p-5 shadow-soft">البنوك</div>
      </div>
    </main>
  );
}
