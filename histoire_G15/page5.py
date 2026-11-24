def page5(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous arrivez au port d'Illumis. Un recruteur vous demande si vous voulez vous engagez dans l'expédition. Vous hésitez mais vous savez que c'est le seul moyen de sauver Illumis.")
    print("1 - Partir directement pour l'expédition   2 - Parler quelques minutes de plus avec le recruteur")
    choix: str = input("> ")

    if choix == "1":
        res = 10
    elif choix == "2":
        res = 6
    else:
        print("Choix invalide.")
        res = 5                  # on reste sur cette page

    return res
