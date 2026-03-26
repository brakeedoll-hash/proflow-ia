
import Layout from "../components/Layout";

export default function Projects() {
  return (
    <Layout>
      <h1 className="text-3xl mb-6">Proyectos</h1>
      <div className="grid md:grid-cols-2 gap-6">
        <div className="p-6 bg-white/5 rounded-2xl">Proyecto IA 1</div>
        <div className="p-6 bg-white/5 rounded-2xl">Proyecto IA 2</div>
      </div>
    </Layout>
  );
}
