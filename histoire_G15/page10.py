def page10(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    if gameState["culpabilité"] == False:
        print("Vous embarquez avec l'équipage vers le continent inconnu. Le sentiment de culpabilité de par l'abandon de votre jeune soeur se fait toujours ressentir.")
    elif gameState["culpabilité"] == True:
        print("Vous embarquez avec votre soeur et l'équipage vers le continent inconnu. Votre soeur est contente d'être avec vous.")

    print("1 - Continuer vers le continent inconnu")
    choix: str = input("> ")

    if choix == "1":
        res = 11
    else:
        print("Choix invalide.")
        res = 10                  # on reste sur cette page

    return res
