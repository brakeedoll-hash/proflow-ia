import Groq from "groq-sdk";

const groq = new Groq({ 
  apiKey: process.env.GROQ_API_KEY 
});

export const POST = async ({ request }) => {
  try {
    const { message } = await request.json();
    const completion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres ProFlow AI, asistente de hardware. Responde breve y técnico con emojis." },
        { role: "user", content: message },
      ],
      model: "llama3-8b-8192",
    });
    return new Response(JSON.stringify({ response: completion.choices[0].message.content }), { status: 200 });
  } catch (error) {
    return new Response(JSON.stringify({ error: "Error de conexión." }), { status: 500 });
  }
};
