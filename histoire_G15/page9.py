def page9(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous avez perdu, vous décidez d'offrir un picto de vitesse ou de force.")
    print("1 - Offrir un picto de vitesse   2 - Offrir un picto de soin")
    choix: str = input("> ")

    if choix == "1":
        gameState["vitesse"] = gameState["vitesse"] - 6
        print("Votre vitesse diminue de 5. Elle est maintenant de:", gameState["vitesse"])
        res = 10
    elif choix == "2":
        gameState["force"] = gameState["force"] - 5
        print("Votre force diminue de 5. Elle est maintenant de:", gameState["force"])
        res = 10
    else:
        print("Choix invalide.")
        res = 9                  # on reste sur cette page

    return res
