import os
from openai import OpenAI

class OpenRouter:
    
    def inicio(text, gui_reference=None):
        
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
            messages=[
                {"role": "user", "content": prompt}
            ],
            extra_headers={
                "HTTP-Referer": "https://0t4v14n0.github.io/portfolio/",
                "X-Title": "Di gue ?",
            }
        )

        print(completion.choices[0].message.content)

        if gui_reference:
            # Atualiza a GUI na thread principal
            gui_reference.after(0, lambda: gui_reference.mostrar_resposta(completion.choices[0].message.content))