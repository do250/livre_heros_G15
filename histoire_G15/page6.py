def page6(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Le recruteur veut jauger votre niveau. Cependant l'embarcation approche, le temps presse. Il vous propose un pile ou face. Si vous devinez le bon côté de la pièce, vous recevrez une récompense. En revanche, si vous vous trompez vous devrez lui donner quelque chose.")
    print("1 - Accepter de jouer   2 - Refuser de jouer")
    choix: str = input("> ")

    if choix == "1":
        res = 7
    elif choix == "2":
        res = 10
    else:
        print("Choix invalide.")
        res = 6                  # on reste sur cette page

    return res
