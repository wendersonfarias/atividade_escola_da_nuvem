
# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. 
# Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta"
preco_original = 50.00
desconto = 20.00
valor_final = (preco_original)*(100-desconto)/100;
valor_descontado = preco_original*(desconto/100)

print(f"O valor total do item {nome_produto} é R${preco_original}")
print(f"ele tem {desconto} % de desconto")
print(f"O valor final com desconto é {valor_final:.2f} com desconto de R${valor_descontado:.2f}")