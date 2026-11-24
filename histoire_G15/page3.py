def page3(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("En regardant le carnet, vous découvez des paysages du continent inconnus. Sophie vous raconte qu'elle voit ces paysages dans ses rêves.")
    print("Vous expliquez à Sophie, que vous allez partir à l'expédition. Sophie à très envie de venir avec vous, mais l'expédition est trop dangereuse et Sophie risque d'y laisser sa vie.")
    print("1 - Lui demander de venir avec vous   2 - La laisser et partir sans elle")
    choix: str = input("> ")

    if choix == "1":
        res = 4
    elif choix == "2":
        print("Un sentiment de culpabilité vous envahi.")
        gameState["culpabilité"] = True
        res = 5
    else:
        print("Choix invalide.")
        res = 3                  # on reste sur cette page

    return res
