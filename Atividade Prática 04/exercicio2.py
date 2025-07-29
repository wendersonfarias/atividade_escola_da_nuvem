# 2 - Criar um código que registre as notas de alunos,
# e calcular a média da turma.

def registrar_notas():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
        if nota.lower() == "sair":
            break
        try:
            notas.append(float(nota))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota registrada.")

registrar_notas()
