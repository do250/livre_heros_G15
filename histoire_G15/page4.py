def page4(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Sophie toute souriante, se dirige, avec vous, vers le port.")
    print("1 - Aller au port")
    choix: str = input("> ")

    if choix == "1":
        res = 5
    else:
        print("Choix invalide.")
        res = 4                  # on reste sur cette page

    return res
