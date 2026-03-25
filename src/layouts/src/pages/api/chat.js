import Groq from "groq-sdk";

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

export const POST = async ({ request }) => {
  try {
    const { message } = await request.json();
    const completion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres ProFlow AI. Responde técnico y breve con emojis de hardware." },
        { role: "user", content: message }
      ],
      model: "llama3-8b-8192",
    });
    return new Response(JSON.stringify({ response: completion.choices[0].message.content }), { status: 200 });
  } catch (e) {
    return new Response(JSON.stringify({ error: "Error de conexión con el núcleo." }), { status: 500 });
  }
};
