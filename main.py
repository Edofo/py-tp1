import requests  # Importation de la bibliothèque requests
from endpoints import BASE_URL, POSTS, USERS  # Importation des constantes


def get_data(endpoint, limit=5):  # limit=5 est une valeur par défaut
    response = requests.get(BASE_URL + endpoint, params={"_limit": limit})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données depuis {endpoint}")
        return []


def get_posts():  # Fonction pour obtenir des articles
    posts = get_data(POSTS)
    for post in posts:
        print(f"Titre: {post['title']}")


def get_users():  # Fonction pour obtenir des utilisateurs
    users = get_data(USERS)
    for user in users:
        print(f"Nom de l'utilisateur: {user['name']}")


def create_post():  # Fonction pour créer un article
    title = input("Entrez le titre de l'article: ")
    body = input("Entrez le corps de l'article: ")

    data = {
        "title": title,
        "body": body,
        "userId": 1  # Vous pouvez modifier l'ID de l'utilisateur ici
    }

    response = requests.post(BASE_URL + POSTS, json=data)

    if response.status_code == 201:
        new_post = response.json()
        print(f"ID du nouvel article créé: {new_post['id']}")
    else:
        print("Erreur lors de la création de l'article")


def main():  # Fonction principale
    while True:
        print("Menu:")
        print("1. Obtenir des articles")
        print("2. Obtenir des utilisateurs")
        print("3. Créer un article")
        print("4. Quitter")

        choix = input("Choisissez une option (1/2/3/4): ")

        if choix == "1":
            get_posts()
        elif choix == "2":
            get_users()
        elif choix == "3":
            create_post()
        elif choix == "4":
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main()
