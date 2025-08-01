from datetime import datetime

# 4 - Crie um programa que calcule a quantos dias um individuo 
# está vivo de acordo com a data do dia.

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.now()
dias_vivo = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")