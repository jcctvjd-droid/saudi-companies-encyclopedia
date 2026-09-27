export default function CompanyPage({ params }: { params: { id: string } }) {
  return (
    <main className="mx-auto max-w-5xl px-4 py-8">
      <h1 className="mb-6 text-3xl font-black text-slate-900">تفاصيل الشركة</h1>
      <div className="rounded-3xl bg-white p-6 shadow-soft">
        <p className="text-xl font-bold">الشركة #{params.id}</p>
        <div className="mt-6 grid gap-6 md:grid-cols-2">
          <div className="rounded-xl bg-slate-50 p-4"><strong>الاسم العربي:</strong> <span>شركة الاتصالات السعودية</span></div>
          <div className="rounded-xl bg-slate-50 p-4"><strong>الاسم الإنجليزي:</strong> <span>Saudi Telecom Company</span></div>
          <div className="rounded-xl bg-slate-50 p-4"><strong>نوع الشركة:</strong> <span>Public</span></div>
          <div className="rounded-xl bg-slate-50 p-4"><strong>الحالة:</strong> <span>Active</span></div>
        </div>
      </div>
    </main>
  );
}
