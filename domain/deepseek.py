import requests
import os

key = os.getenv("key-api-deepseek")

# Substitua pela sua chave de API do OpenRouter
API_KEY = key
API_URL = 'https://openrouter.ai/api/v1'

# Defina os cabeçalhos para a requisição da API
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Defina o payload da requisição (dados)
data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "Qual é o significado da vida?"}]
}

# Envie a requisição POST para a API DeepSeek
response = requests.post(API_URL, json=data, headers=headers)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Resposta da API:", response.json())
else:
    print("Falha ao buscar dados da API. Código de Status:", response.status_code)