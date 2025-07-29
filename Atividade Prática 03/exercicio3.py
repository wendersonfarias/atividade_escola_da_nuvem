# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas 
# entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, 
# a unidade de origem e a unidade para qual deseja converter.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == unidade_destino:
        return valor
    if unidade_origem == "Celsius":
        if unidade_destino == "Fahrenheit":
            return celsius_to_fahrenheit(valor)
        elif unidade_destino == "Kelvin":
            return celsius_to_kelvin(valor)
    elif unidade_origem == "Fahrenheit":
        if unidade_destino == "Celsius":
            return fahrenheit_to_celsius(valor)
        elif unidade_destino == "Kelvin":
            return fahrenheit_to_kelvin(valor)
    elif unidade_origem == "Kelvin":
        if unidade_destino == "Celsius":
            return kelvin_to_celsius(valor)
        elif unidade_destino == "Fahrenheit":
            return kelvin_to_fahrenheit(valor)
    return None  # Caso unidades inválidas

def normalizar_unidade(letra):
    letra = letra.lower()
    if letra == "c":
        return "Celsius"
    elif letra == "f":
        return "Fahrenheit"
    elif letra == "k":
        return "Kelvin"
    else:
        return None

if __name__ == "__main__":
    valor = float(input("Digite o valor da temperatura: "))
    unidade_origem = normalizar_unidade(input("Digite a unidade de origem (C, F, K): "))
    unidade_destino = normalizar_unidade(input("Digite a unidade de destino (C, F, K): "))
    resultado = converter_temperatura(valor, unidade_origem, unidade_destino)
    if resultado is not None:
        print(f"{valor} {unidade_origem} = {resultado:.2f} {unidade_destino}")
    else:
        print("Unidade inválida!")