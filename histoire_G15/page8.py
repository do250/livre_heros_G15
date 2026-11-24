def page8(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Comme promis le recruteur vous offre une récompense. Vous avez le choix entre un picto de vie et un picto de force.")
    print("1 - Prendre le picto de vie   2 - Prendre le picto de soin")
    choix: str = input("> ")

    if choix == "1":
        gameState["vie"] = gameState["vie"] + 5
        print("Votre vie augmente de 5. Elle est maintenant de:", gameState["vie"])
        res = 10
    elif choix == "2":
        gameState["force"] = gameState["force"] + 5
        print("Votre force augmente de 5. Elle est maintenant de:", gameState["force"])
        res = 10
    else:
        print("Choix invalide.")
        res = 8                  # on reste sur cette page

    return res
