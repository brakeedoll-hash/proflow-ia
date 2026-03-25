import Groq from "groq-sdk";

// Configuramos la API Key (Asegúrate de tenerla en Vercel como GROQ_API_KEY)
const apiKey = process.env.GROQ_API_KEY || import.meta.env.GROQ_API_KEY;
const groq = new Groq({ apiKey: apiKey });

export const POST = async ({ request }) => {
  try {
    const body = await request.json();
    const { message } = body;

    if (!message) {
      return new Response(JSON.stringify({ error: "No enviaste un mensaje" }), { status: 400 });
    }

    const completion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres el asistente avanzado de ProFlow IA. Responde de forma clara y profesional." },
        { role: "user", content: message },
      ],
      model: "llama3-8b-8192", // Modelo estable
      temperature: 0.7,
    });

    const responseText = completion.choices[0].message.content;

    return new Response(JSON.stringify({ response: responseText }), {
      status: 200,
      headers: { "Content-Type": "application/json" }
    });

  } catch (error) {
    console.error("Error en API v2:", error);
    return new Response(JSON.stringify({ error: "La IA está saturada, intenta en un momento." }), { 
      status: 500 
    });
  }
};
