export const GET = async () => {
  try {
    const API_KEY = process.env.GEMINI_API_KEY;
    
    // 1. Le pedimos a Gemini una noticia real de Marzo 2026
    const prompt = "Genera una noticia técnica real de marzo 2026 sobre hardware o redes en Costa Rica. Devuelve SOLO el contenido en formato Markdown con este frontmatter: --- title: 'Titulo' fecha: '2026-03-25' --- y luego el desarrollo.";
    
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }]
      })
    });

    const data = await response.json();
    const newsContent = data.candidates[0].content.parts[0].text;

    // Nota: En Vercel Serverless no podemos escribir archivos físicamente en el disco duro,
    // pero podemos hacer que esta API devuelva la noticia para mostrarla.
    
    return new Response(JSON.stringify({ news: newsContent }), { 
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: "El bot de noticias está fuera de servicio." }), { status: 500 });
  }
};
