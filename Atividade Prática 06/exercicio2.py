import requests

# 2 - Crie um programa que gera um perfil de usuário aleatório usando a
# API 'Random User Generator'. O programa deve exibir o nome, email e
# país do usuário gerado."

response = requests.get('https://randomuser.me/api/')
if response.status_code == 200:
    data = response.json()
    user = data['results'][0]
    nome = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    pais = user['location']['country']
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao obter dados do usuário.")