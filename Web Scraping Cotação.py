import requests
from bs4 import BeautifulSoup

# Insere a url que quer fazer a raspagem
url = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&'

# Mostra que é um navegador requisitando
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}

# Faze a requisição
requisicao = requests.get(url, headers=headers)

# Verifica o status da requisição
if requisicao.status_code == 200:
    print("Sucesso")
else:
    print(f"Erro: {requisicao.status_code}")

# Lê a linha em html
soup = BeautifulSoup(requisicao.content, 'html.parser')

# Exibe o título da página
title = soup.title.text
print(title)

# Encontra e formata o valor do dólar
span = soup.find('span', class_='DFlfde SwHCTb')
if span:
    valor = span['data-value']
    valor_formatado = f"{float(valor):.2f}"
    print(f'Valor do dólar hoje: {valor_formatado} em Reais')
else:
    print("Não foi possível encontrar o valor do dólar.")
