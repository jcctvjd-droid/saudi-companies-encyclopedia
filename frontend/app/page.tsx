import Link from "next/link";

const filters = [
  { label: "القطاع", value: "sector" },
  { label: "المدينة", value: "city" },
  { label: "المنطقة", value: "region" },
  { label: "النشاط", value: "activity" },
  { label: "نوع الشركة", value: "company_type" },
  { label: "الحالة", value: "status" },
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-slate-100">
      <header className="mx-auto max-w-7xl px-4 py-6">
        <nav className="flex items-center justify-between"> 
          <div className="text-xl font-bold text-brand-900">موسوعة الشركات السعودية</div>
          <div className="flex gap-4 text-sm text-slate-600">
            <Link href="/companies">البحث</Link>
            <Link href="/sectors">القطاعات</Link>
            <Link href="/cities">المدن</Link>
            <Link href="/regions">المناطق</Link>
            <Link href="/map">الخريطة</Link>
          </div>
        </nav>
      </header>

      <section className="mx-auto max-w-5xl px-4 pb-10 pt-8">
        <div className="rounded-3xl bg-white p-6 shadow-soft md:p-10">
          <p className="mb-3 text-sm font-medium text-brand-700">محرك بحث وموسوعة للشركات والمنشآت التجارية</p>
          <h1 className="text-3xl font-black text-slate-900 md:text-5xl">موسوعة الشركات السعودية</h1>
          <p className="mt-4 max-w-2xl text-base text-slate-600 md:text-lg">
            محرك بحث وموسوعة للشركات والمنشآت التجارية في المملكة العربية السعودية.
          </p>

          <div className="mt-8 flex flex-col gap-3 rounded-2xl border border-slate-200 bg-slate-50 p-3 md:flex-row md:items-center">
            <input
              className="w-full rounded-xl border border-slate-200 bg-white px-4 py-3 text-right outline-none ring-0 focus:border-brand-500"
              placeholder="ابحث عن شركة أو مؤسسة أو نشاط…"
            />
            <button className="rounded-xl bg-brand-700 px-5 py-3 font-bold text-white shadow-sm hover:bg-brand-900">
              بحث
            </button>
          </div>

          <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {filters.map((item) => (
              <div key={item.value} className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-right">
                <label className="mb-2 block text-sm text-slate-600">{item.label}</label>
                <select className="w-full rounded-lg border border-slate-200 bg-white px-3 py-2 text-right">
                  <option>الكل</option>
                </select>
              </div>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
