#1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. 
#Use os seguintes dados:

#* Valor em reais: R$ 100.00
#* Taxa do dólar: R$ 5.20
#* Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, 
#arredondando para duas casas decimais.

reais = 100.00
dolar = 5.20
euro = 6.15

dolar_convertido = reais /dolar
euro_convertido = reais / euro

print(f"O valor de R${reais} convertido em dolar é USD:{dolar_convertido:.2f} .")
print(f"O valor de R${reais} convertido em euro é EUR:{euro_convertido:.2f} .")