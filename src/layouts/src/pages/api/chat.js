import Groq from "groq-sdk";

// Usamos la Key directamente para eliminar errores de Vercel
const groq = new Groq({ 
  apiKey: "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" 
});

export async function POST({ request }) {
  try {
    const { mensaje } = await request.json();

    const chatCompletion = await groq.chat.completions.create({
      messages: [
        { 
          role: "system", 
          content: "Eres la IA de ProFlow. Hoy es marzo 2026. Responde de forma técnica, real y transparente sobre hardware e IA. No inventes datos." 
        },
        { role: "user", content: mensaje }
      ],
      // Usamos un modelo estándar muy estable en Groq
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
    console.error("Error en Groq:", error);
    return new Response(JSON.stringify({ 
      respuesta: "Error: " + error.message 
    }), { 
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
}
