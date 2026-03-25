import Groq from "groq-sdk";

const groq = new Groq({ 
  apiKey: process.env.GROQ_API_KEY 
});

export const POST = async ({ request }) => {
  try {
    const { message } = await request.json();

    const completion = await groq.chat.completions.create({
      messages: [
        { role: "system", content: "Eres ProFlow AI, un asistente experto en hardware y sistemas. Responde de forma breve, técnica y con emojis tech." },
        { role: "user", content: message },
      ],
      model: "llama3-8b-8192",
      temperature: 0.6,
    });

    return new Response(JSON.stringify({ 
      response: completion.choices[0].message.content 
    }), { status: 200 });

  } catch (error) {
    return new Response(JSON.stringify({ 
      error: "Error de conexión con el núcleo de IA." 
    }), { status: 500 });
  }
};
