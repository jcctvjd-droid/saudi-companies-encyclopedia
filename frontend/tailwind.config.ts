import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#eef7ff",
          100: "#d8ecff",
          500: "#0a5fbd",
          700: "#05458a",
          900: "#022d55",
        },
      },
      boxShadow: {
        soft: "0 10px 30px rgba(10, 95, 189, 0.12)",
      },
    },
  },
  plugins: [],
};

export default config;
