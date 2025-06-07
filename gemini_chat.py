# To run this code you need to install the following dependencies:
# pip install google-genai

from dotenv import load_dotenv
import os

# Carregar o arquivo .env
load_dotenv()

# Verificar se a variável foi carregada
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("A variável GOOGLE_API_KEY não foi encontrada. Verifique o arquivo .env.")

print(f"API Key carregada: {api_key}")

from google import genai
from google.genai import types


def generate():
    client = genai.Client(
         api_key=api_key,
    )
    # TAREFA 1: escolher o modelo apropriado e ajustar entrada do usuário e retorno da função


if __name__ == "__main__":
#    # Teste para ter certeza que funciona
    test_response = generate(entrada="Olá, como está o tempo hoje em Cuiabá?")
    print(f"Test response: {test_response}")