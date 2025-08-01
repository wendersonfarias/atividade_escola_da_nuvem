# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
# baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado 
# no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcula_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    Parâmetros:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    Retorna:
        float: O valor da gorjeta calculada
    """
    return valor_conta * (porcentagem_gorjeta / 100)


# Execução interativa:
if __name__ == "__main__":
    try:
        valor = float(input("Digite o valor total da conta: "))
        porcentagem = float(input("Digite a porcentagem da gorjeta: "))
        gorjeta = calcula_gorjeta(valor, porcentagem)
        print(f"Gorjeta: R$ {gorjeta:.2f}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

