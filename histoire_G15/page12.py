def page12(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous vous approchez du vieil homme. Il vous souhaite la bienvenue. Vous lui expliquez que vous êtes ici pour arrêter la gomme. L'homme vous explique que pour arrêter cette dernière, il faut récupérer 3 fragments du picto-mère. Il vous explique qu'il suffit d'aller explorer les différents chemins présent. Il vous avertit cependant que les Ruines de l'Atelier sont occupées par la peintresse. Le vieil homme vous souhaite bonne chance !")
    print("1 - Continuer")
    choix: str = input("> ")

    if choix == "1":
        res = 13
    else:
        print("Choix invalide.")
        res = 12                  # on reste sur cette page

    return res
