def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous vous réveillez à Illumis, la cloche retentit. La gomme est passé cette nuit. Chaque année, la peintresse passe et efface un centième de la population. Cela dure depuis pas moins de 67 ans. Cette nuit votre voisin a disparu.")
    print("Votre soeur arrive devant vous, persuader que tout va sombrer.")
    print("1 - Consoler votre soeur (Sophie)   2 - Aller voir l'expédition qui se prépare au port")
    choix: str = input("> ")

    if choix == "1":
        res = 2
    elif choix == "2":
        res = 5
    else:
        print("Choix invalide.")
        res = 1                  # on reste sur cette page

    return res
