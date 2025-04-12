# import requests
import os
from openai import OpenAI

class OpenRouter:
    
    def inicio(text):
        
        key = os.getenv("key-api-deepseek")

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=key,
        )

        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "user", "content": text}
            ],
            extra_headers={
                "HTTP-Referer": "https://seusite.com",
                "X-Title": "Meu App",
            }
        )

        print(completion.choices[0].message.content)