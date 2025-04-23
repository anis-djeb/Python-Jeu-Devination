# Importation du module random pour générer des nombres aléatoires
import random

# Génère un nombre aléatoire entre 1 et 10
nombre_secret = random.randint(1, 10)
tentatives = 0

while True:
    nombre_propose = int(input("Entrez un nombre entre 1 et 10 : "))
    tentatives += 1

    if nombre_propose == nombre_secret:
        print("Bravo ! Seriez-vous un devin ? Continuez comme ça, Harry ! Vous avez deviné en", tentatives, "tentatives.")
        break

    elif nombre_propose < nombre_secret:
        print("Ce n'est pas tout à fait ça. Ne visez pas si bas. Le ciel est la limite ! Déployez vos ailes ! Jusqu'à présent, vous avez fait", tentatives, "tentatives.")
        nombre_secret = random.randint(1, 10)  # Re-génère un nouveau nombre

    else:
        print("Ce n'est pas tout à fait ça. Vous avez visé trop haut. Bien que cela soit compréhensible, parfois la solution est juste sous nos yeux. Continuez à chercher ! Jusqu'à présent, vous avez fait", tentatives, "tentatives.")
        nombre_secret = random.randint(1, 10)  # Re-génère un nouveau nombre