import requests

# 3 - Desenvolva um programa que consulte informações de
# endereço a partir de um CEP fornecido pelo usuário, utilizando
# a API ViaCEP. O programa deve exibir o logradouro, bairro,
# cidade e estado correspondentes ao CEP consultado.

cep = input("Digite o CEP (somente números): ").strip()
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if "erro" in data:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {data.get('logradouro', 'N/A')}")
        print(f"Bairro: {data.get('bairro', 'N/A')}")
        print(f"Cidade: {data.get('localidade', 'N/A')}")
        print(f"Estado: {data.get('uf', 'N/A')}")
except requests.RequestException:
    print("Erro ao consultar o CEP.")