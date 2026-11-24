import random

def page15(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("En prenant le chemin court vous passez sur le bord d'un ravin. Une corde permet de continuer le chemin. Cependant, la corde semble fragile et risque de rompre.")

    vent: str = random.choices(["Le vent souffle fort", "Le vent est calme"], weights=[40, 60])[0] # choisi une valeur aléatoire (pondérée grâce à "weights") entre "Le vent souffle fort" (25%) et "Le vent est calme" (75%). Le [0] permet de retourner une chaine de caractère, sans le [0], random.choice renvoie la liste contenant le résultat du tirage.

    if vent == "Le vent souffle fort":
        gameState["vent_fort"] = True
        print(vent)
    else:
        print(vent)

    print("1 - Utiliser la corde   2 - Faire retour arrière et prendre le chemin long")
    choix: str = input("> ")



    if choix == "1":
        res = 16
    elif choix == "2":
        res = ? #page chemin long
    else:
        print("Choix invalide.")
        res = 15                  # on reste sur cette page

    return res
