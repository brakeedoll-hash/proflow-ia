
import Layout from "../components/Layout";

export default function Home() {
  return (
    <Layout>
      <section className="text-center mt-20">
        <h1 className="text-6xl font-bold mb-6 bg-gradient-to-r from-blue-500 to-cyan-400 text-transparent bg-clip-text">
          Construye con IA
        </h1>
        <p className="text-gray-400 mb-8">
          Plataforma rápida, moderna y minimalista con IA
        </p>
        <div className="flex justify-center gap-4">
          <button className="bg-blue-500 px-6 py-3 rounded-2xl hover:scale-105 transition">
            Empezar
          </button>
          <button className="border border-white/20 px-6 py-3 rounded-2xl hover:bg-white/10 transition">
            Demo
          </button>
        </div>
      </section>

      <section className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 bg-white/5 rounded-2xl">⚡ Ultra rápido</div>
        <div className="p-6 bg-white/5 rounded-2xl">🧠 IA avanzada</div>
        <div className="p-6 bg-white/5 rounded-2xl">🛠️ Tools</div>
      </section>
    </Layout>
  );
}
