# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
# Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
# incluindo o resultado final arredondado para duas casas decimais.

distancia_percorrida = 300.00
combustivel_gasto = 25.00
consumo_medio = 300 / 25
print("A viagem foi concluida com sucesso!")
print(f"Dados da vigem: distancia percorrida = {distancia_percorrida} km, combustivel gasto = {combustivel_gasto} L")
print(f"O consumo médio é {consumo_medio:.2f} (km/l)")