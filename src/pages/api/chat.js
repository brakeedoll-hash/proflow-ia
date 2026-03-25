export const prerender = false;

export const POST = async ({ request }) => {
  try {
    const { message } = await request.json();
    const API_KEY = import.meta.env.GEMINI_API_KEY || process.env.GEMINI_API_KEY;

    if (!API_KEY) {
      return new Response(JSON.stringify({ error: "API key no configurada." }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{
            parts: [{ text: `Eres ProFlow AI, un asistente técnico experto en hardware y redes. Responde breve y con emojis tech. Pregunta: ${message}` }]
          }]
        })
      }
    );

    const data = await response.json();

    if (!data.candidates || !data.candidates[0]) {
      return new Response(JSON.stringify({ error: "Respuesta vacía del modelo." }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const aiResponse = data.candidates[0].content.parts[0].text;

    return new Response(JSON.stringify({ response: aiResponse }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: "Núcleo Gemini fuera de línea." }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};
