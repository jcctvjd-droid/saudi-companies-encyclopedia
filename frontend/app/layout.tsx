import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Saudi Companies Encyclopedia",
  description: "Search and explore companies in Saudi Arabia.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ar" dir="rtl">
      <body className="bg-slate-50 text-slate-900 antialiased">{children}</body>
    </html>
  );
}
