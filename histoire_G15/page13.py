def page13(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Trois chemins s'offrent à vous.")
    print("Se diriger vers :")
    print("1 - La Falaise des Pictos  2 - La Forêt Blanche  3 - Les Ruines de l'Atelier")
    choix: str = input("> ")

    if choix == "1":
        res = 14
    elif choix == "2":
        res = ? #1ere page foret blanche
    elif choix == "3":
        res = ? #1ere page ruines ateliers
    else:
        print("Choix invalide.")
        res = 13                  # on reste sur cette page

    return res