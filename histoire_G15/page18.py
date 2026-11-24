def page18(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("")
    print("1 - choi1   2 - choix2")
    choix: str = input("> ")

    if choix == "1":
        res = 99
    elif choix == "2":
        res = 99 
    else:
        print("Choix invalide.")
        res = 18                  # on reste sur cette page

    return res 
