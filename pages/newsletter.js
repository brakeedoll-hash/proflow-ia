
import Layout from "../components/Layout";

export default function Newsletter() {
  return (
    <Layout>
      <div className="text-center mt-20">
        <h1 className="text-4xl mb-4">Newsletter</h1>
        <p className="text-gray-400 mb-6">
          Recibe contenido exclusivo de IA
        </p>
        <input className="p-3 rounded-xl bg-white/10 mb-3 w-64" placeholder="Email" />
        <br />
        <button className="bg-blue-500 px-6 py-2 rounded-xl">
          Suscribirme
        </button>
      </div>
    </Layout>
  );
}
