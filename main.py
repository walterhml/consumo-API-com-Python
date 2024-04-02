import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Erro ao acessar a API do GitHub: {response.status_code}")
        return None

#como usar:
username = input("Digite o nome de usuário do GitHub: ")
user_info = get_github_user_info(username)

if user_info:
    print("Informações do usuário:")
    print(f"Nome: {user_info['name']}")
    print(f"Localização: {user_info['location']}")
    print(f"Bio: {user_info['bio']}")
else:
    print("Usuário não encontrado ou erro ao acessar a API do GitHub.")
