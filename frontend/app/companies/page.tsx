export default function CompaniesPage() {
  return (
    <main className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-4 text-3xl font-black text-slate-900">نتائج البحث</h1>
      <div className="rounded-2xl bg-white p-5 shadow-soft">
        <div className="grid gap-4 border-b border-slate-200 pb-4 md:grid-cols-5">
          <div><strong>اسم الشركة</strong></div>
          <div><strong>القطاع</strong></div>
          <div><strong>المدينة</strong></div>
          <div><strong>نوع الشركة</strong></div>
          <div><strong>الحالة</strong></div>
        </div>
        <div className="mt-4 rounded-xl bg-slate-50 p-4">
          <p className="text-slate-600">DEMO DATA: لا توجد نتائج حاليًا.</p>
        </div>
      </div>
    </main>
  );
}
