
import Layout from "../components/Layout";
import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const send = () => {
    if (!input) return;
    setMessages([...messages, { role: "user", text: input }]);
    setInput("");
  };

  return (
    <Layout>
      <h1 className="text-2xl mb-4">Chat IA</h1>
      <div className="h-[60vh] overflow-y-auto p-4 bg-white/5 rounded-2xl mb-4">
        {messages.map((m, i) => (
          <div key={i} className={m.role === "user" ? "text-right" : ""}>
            <div className="inline-block px-4 py-2 rounded-2xl bg-blue-500/20 mb-2">
              {m.text}
            </div>
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-3 rounded-xl bg-white/10"
          placeholder="Escribe aquí..."
        />
        <button onClick={send} className="bg-blue-500 px-4 rounded-xl">
          Enviar
        </button>
      </div>
    </Layout>
  );
}
