import Groq from "groq-sdk";

// Intentamos obtener la llave de varias formas para asegurar compatibilidad
const apiKey = process.env.GROQ_API_KEY || import.meta.env.GROQ_API_KEY;

const groq = new Groq({ apiKey: apiKey });

export async function POST({ request }) {
  // Verificamos si la llave existe antes de empezar
  if (!apiKey) {
    return new Response(JSON.stringify({ 
      respuesta: "Error: No se encontró la API KEY de Groq en el servidor." 
    }), { status: 500 });
  }

  const { mensaje } = await request.json();

  try {
    const chatCompletion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres la IA de ProFlow. Hoy es marzo 2026. Responde de forma técnica, real y transparente. No inventes datos si no los sabes." },
        { role: "user", content: mensaje }
      ],
      model: "llama-3.3-70b-versatile",
      temperature: 0.5,
    });

    return new Response(JSON.stringify({
      respuesta: chatCompletion.choices[0].message.content
    }), { status: 200 });

  } catch (error) {
    return new Response(JSON.stringify({ 
      respuesta: "Error conectando con el cerebro de la IA. Detalle: " + error.message 
    }), { status: 500 });
  }
}
