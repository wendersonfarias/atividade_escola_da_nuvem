# 3 - Criar um código que serve para verificar se uma senha digitada 
# pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
# Solicita a senha do usuário

senha = input("Digite uma senha: ")

# Verifica se a senha tem pelo menos 8 caracteres
tem_8_caracteres = len(senha) >= 8

# Verifica se a senha contém pelo menos um número
tem_numero = any(char.isdigit() for char in senha)

# Exibe o resultado
if tem_8_caracteres and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
