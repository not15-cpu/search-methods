import os
import google.generativeai as genai
from dotenv import load_dotenv
# Substitua pela sua chave de API do Gemini
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Modelo do Gemini para geração de texto
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

def buscar_e_resumir_noticias_gemini(query="notícias sobre a economia do Brasil e a possível crise hidrica no mundo"):
    """Pede ao Gemini para buscar e resumir notícias."""
    prompt = f"""Realize uma busca na internet por notícias recentes sobre "{query}".
    Após encontrar algumas fontes relevantes, resuma brevemente (3-5 frases) os principais eventos e informações encontradas.
    Inclua também os links para as fontes que você utilizou para gerar o resumo.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao obter resposta do Gemini: {e}")
        return "Erro ao buscar e resumir notícias."

if __name__ == "__main__":
    print("Pedindo ao Gemini para buscar e resumir notícias do mundo...")
    resultado = buscar_e_resumir_noticias_gemini()
    print("\n--- Resultado do Gemini ---")
    print(resultado)