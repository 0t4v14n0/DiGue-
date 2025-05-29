import os
from openai import OpenAI

class OpenRouter:
    
    def inicio(text, gui_reference=None):

        try:
        
            key = os.getenv("key-api-deepseek")

            prompt = f"""
            Você é um assistente especializado em responder questões de múltipla escolha.
            Siga estas regras:
            1. Analise o texto abaixo (extraído via OCR, pode conter erros).
            2. Identifique a pergunta e as alternativas.
            3. Responda APENAS com a letra da alternativa correta, seguida de parênteses.
            4. Se não reconhecer a resposta, retorne "X) Não identificado".
            5. Lembre de responder o mais breve possivel

            Texto do OCR:
            {text}
            """

            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=key,
            )

            completion = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                extra_headers={
                    "HTTP-Referer": "https://0t4v14n0.github.io/portfolio/",
                    "X-Title": "Di gue ?",
                }
            )

            response = completion.choices[0].message.content
            print(response)

            if gui_reference:
                gui_reference.after(0, lambda: gui_reference.mostrar_resposta_api(response))

        except:

            print("Ocorreu um erro na API ou esta sem internet")
            gui_reference.after(0, "Ocorreu um erro na API ou esta sem internet")