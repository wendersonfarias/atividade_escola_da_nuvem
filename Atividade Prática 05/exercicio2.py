# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
def eh_palindromo(frase: str) -> bool:
    # Remove espaços e pontuação, e converte para minúsculas
    frase = ''.join(c.lower() for c in frase if c.isalnum())
    # Verifica se a frase é igual ao seu reverso
    return frase == frase[::-1]

# Execução interativa:
if __name__ == "__main__":
    texto = input("Digite uma palavra ou frase: ")
    if eh_palindromo(texto):
        print("Sim")
    else:
        print("Não")
