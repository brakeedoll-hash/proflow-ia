import Groq from "groq-sdk";

// Esta línea busca la llave de forma segura en el servidor de Vercel
const apiKey = process.env.GROQ_API_KEY || import.meta.env.GROQ_API_KEY;

const groq = new Groq({ apiKey: apiKey });

export async function POST({ request }) {
  if (!apiKey) {
    return new Response(JSON.stringify({ 
      respuesta: "Error: Configuración de seguridad pendiente en el servidor." 
    }), { status: 500 });
  }

  try {
    const { mensaje } = await request.json();

    const chatCompletion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres la IA de ProFlow. Responde de forma técnica y real sobre hardware e IA." },
        { role: "user", content: mensaje }
      ],
      model: "llama3-8b-8192",
      temperature: 0.6,
    });

    return new Response(JSON.stringify({
      respuesta: chatCompletion.choices[0].message.content
    }), { 
      status: 200,
      headers: { "Content-Type": "application/json" }
    });

  } catch (error) {
    return new Response(JSON.stringify({ 
      respuesta: "La IA está procesando mucha información. Intenta de nuevo en un momento." 
    }), { status: 500 });
  }
}
