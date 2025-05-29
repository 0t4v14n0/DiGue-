import os
from openai import OpenAI

class OpenRouter:
    @staticmethod
    def inicio(text, gui_reference=None):
        try:
            key = os.getenv("key-api-deepseek")
            if not key:
                raise ValueError("API key não encontrada")
            
            prompt = f"""Você é um assistente especializado em responder questões de múltipla escolha.
            Siga estas regras:
            1. Analise o texto abaixo (extraído via OCR, pode conter erros).
            2. Identifique a pergunta e as alternativas.
            3. Responda APENAS com a letra da alternativa correta, seguida de parênteses.
            4. Se não reconhecer a resposta, retorne "X) Não identificado".
            5. Lembre de responder o mais breve possível

            Texto do OCR:
            {text}"""
            
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
                
        except APIConnectionError as e:
            error_msg = f"Erro de conexão: {str(e)}"
            print(error_msg)
            if gui_reference:
                gui_reference.after(0, lambda: gui_reference.mostrar_erro(error_msg))
        except Exception as e:
            error_msg = f"Erro na API: {str(e)}"
            print(error_msg)
            if gui_reference:
                gui_reference.after(0, lambda: gui_reference.mostrar_erro(error_msg))