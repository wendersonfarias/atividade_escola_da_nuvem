import requests
from datetime import datetime

# 4 - Crie um programa que consulte a cotação atual de uma moeda
# estrangeira em relação ao Real Brasileiro (BRL). O usuário
# deve informar o código da moeda desejada (ex: USD, EUR, GBP), 
# e o programa deve exibir o valor atual, máximo e mínimo
# da cotação, além da data e hora da última atualização. Utilize
# a API da AwesomeAPI para obter os dados de cotação.

moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    key = f"{moeda}BRL"
    if key in data:
        cotacao = data[key]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo: R$ {cotacao['high']}")
        print(f"Valor mínimo: R$ {cotacao['low']}")
        atualizacao = datetime.fromtimestamp(int(cotacao['timestamp']))
        print(f"Última atualização: {atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Moeda não encontrada ou código inválido.")
except Exception as e:
    print("Erro ao consultar a cotação:", e)