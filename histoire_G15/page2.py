def page2(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous essayer de consoler votre soeur.")
    print("Vous découvrez que Sophie dessine dans un carnet des endroits d'Illumis inconnus de tous. Vous vous questionnez sur ces images : d'où viennent-elles ?")
    print("1 - Regarder le carnet de Sophie   2 - Laisser Sophie tranquille : elle a envie d'être seul... ")
    choix: str = input("> ")

    if choix == "1":
        res = 3
    elif choix == "2":
        res = 5
    else:
        print("Choix invalide.")
        res = 2                  # on reste sur cette page

    return res
