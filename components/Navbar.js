
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full flex justify-between items-center p-4 border-b border-white/10 bg-black/50 backdrop-blur-md sticky top-0 z-50">
      <h1 className="text-xl font-bold">ProFlow IA</h1>
      <div className="flex gap-6 text-sm text-gray-300">
        <Link href="/">Inicio</Link>
        <Link href="/chat">Chat</Link>
        <Link href="/tools">Tools</Link>
        <Link href="/projects">Proyectos</Link>
        <Link href="/newsletter">Newsletter</Link>
      </div>
    </nav>
  );
}
