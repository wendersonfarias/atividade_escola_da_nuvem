# 3 - Crie um programa que serve para calcular o preço final de um produto após 
# aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

preco = float(input("Digite o preço do produto: R$ "))
desconto_percentual = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco * (desconto_percentual / 100)
preco_final = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")