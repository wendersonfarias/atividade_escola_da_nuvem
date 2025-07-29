# 1 - Criar um código que faça uma calculadora que tenha,
# as operações básicas(+,-,*,/).

def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {resultado}")

calculadora()
