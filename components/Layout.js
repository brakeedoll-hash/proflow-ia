
import Navbar from "./Navbar";

export default function Layout({ children }) {
  return (
    <div className="bg-[#0A0A0A] text-white min-h-screen">
      <Navbar />
      <main className="p-6">{children}</main>
    </div>
  );
}
