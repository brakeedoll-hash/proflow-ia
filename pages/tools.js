
import Layout from "../components/Layout";

const tools = ["Ideas", "Resumidor", "Traductor", "Código"];

export default function Tools() {
  return (
    <Layout>
      <h1 className="text-3xl mb-6">Herramientas</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {tools.map((t, i) => (
          <div key={i} className="p-6 bg-white/5 rounded-2xl hover:scale-105 transition">
            {t}
          </div>
        ))}
      </div>
    </Layout>
  );
}
