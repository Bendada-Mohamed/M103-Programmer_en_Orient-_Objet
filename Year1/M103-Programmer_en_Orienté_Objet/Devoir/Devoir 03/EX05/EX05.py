import requests

# URL de l'API
url = "https://jsonplaceholder.typicode.com/users/2"

try:
    # Effectuer une requête GET
    response = requests.get(url)

    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Récupérer les données JSON
        data = response.json()

        # Afficher les informations récupérées
        print("Informations de l'utilisateur :")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Échec de la requête. Code d'état : {response.status_code}")

except requests.RequestException as e:
    print(f"Erreur de connexion à l'API : {e}")

except ValueError:
    print("Erreur lors de l'analyse du JSON.")
