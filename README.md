# Jeu de Devination en Python

> Pour utiliser ce script Python, assurez-vous que Python version 3.x est installé sur votre système.  
> Vous pouvez également utiliser un éditeur tel que Visual Studio Code avec l'extension Python activée.

## Description

Ce projet propose un jeu simple en Python où l’utilisateur doit deviner un nombre aléatoire compris entre 1 et 10.

### Fonctionnement du jeu :

* Le programme demande à l’utilisateur de deviner un nombre entre 1 et 10 :
```
  while True:
    nombre_propose = int(input("Entrez un nombre entre 1 et 10 : "))
    tentatives += 1
```

* Si la réponse est correcte, un message de félicitations est affiché, ainsi que le nombre de tentatives nécessaires.
```
    if nombre_propose == nombre_secret:
        print("Bravo ! Seriez-vous un devin ? Vous avez deviné en", tentatives, "tentatives.")
        break
```

* Si la réponse est incorrecte, le programme affiche un message spécifique :
  - Si le nombre proposé est inférieur au bon numéro :
```
    elif nombre_propose < nombre_secret:
        print("Ne visez pas si bas... Jusqu'à présent, vous avez fait", tentatives, "tentatives.")
        nombre_secret = random.randint(1, 10)
```
  - Si le nombre proposé est supérieur :
```
    else:
        print("Vous avez visé trop haut... Jusqu'à présent, vous avez fait", tentatives, "tentatives.")
        nombre_secret = random.randint(1, 10)
```

### Améliorations futures

* Créer une interface graphique avec Tkinter.
* Limiter le nombre de tentatives à 3, puis afficher un message du type :
  > "Merci pour votre participation. Veuillez réessayer !"
