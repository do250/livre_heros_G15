def page14(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("En arrivant devant la falaise, vous vous retrouvez devant 2 chemins. L'un paraît risqué mais court, l'autre est trop long pour voir ce qu'il cache.")
    print("1 - Prendre le chemin court   2 - Prendre le chemin long")
    choix: str = input("> ")

    if choix == "1":
        res = 15
    elif choix == "2":
        res = 99 
    else:
        print("Choix invalide.")
        res = 14                  # on reste sur cette page

    return res
