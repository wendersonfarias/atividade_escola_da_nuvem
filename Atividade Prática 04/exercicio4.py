# 4 - Criar um código que serve para analisar números digitados pelo usuário, 
# classificando-os como pares ou ímpares 
# e contabilizando quantos de cada tipo foram inseridos.

pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é par.")
        else:
            impares += 1
            print(f"{numero} é ímpar.")
    except ValueError:
        print("Por favor, digite um número válido ou 'sair'.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")