def page11(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous arrivez sur une plage, un vieil homme est présent.")
    
    if gameState["culpabilité"] == False:
        print("Sophie vous conseille d'aller lui parler car elle l'a déjà vu dans ses rêves. Il pourrait vous donner des informations importantes.")

    print("1 - Aller lui parler  2 - L'ignorer")
    choix: str = input("> ")

    if choix == "1":
        res = 12
    elif choix == "2":
        res = 13
    else:
        print("Choix invalide.")
        res = 11                  # on reste sur cette page

    return res