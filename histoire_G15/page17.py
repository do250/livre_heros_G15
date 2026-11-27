def page17(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous arrivez au sommet. Vous le reconnaissez car il était dessiné dans le carnet de votre soeur. En vous approchant un peu plus vous trouvez un des fragments du picto-mère. Une énigme se dresse devant vous.")
    
    print("énoncé enigme à faire")

    if gameState["culpabilité"] == False:
        print("indice sophie")

    reponse_enigme: str = input("Donner votre réponse\n> ")

    while reponse_enigme != "reponse (chiffre)":
        if reponse_enigme != "reponse (chiffre)":
            gameState["vie"] = gameState["vie"] - 1
            if gameState["vie"] == 0:
                res = -1
            reponse_enigme: str = input("Donner votre réponse\n> ")
            print("Vous avez faux, ...", gameState["vie"])
        elif reponse_enigme == "reponse (chiffre)":
            print("Vous avez réussi l'énigme !")




    print("1 - Prendre le fragment du picto-mère et retourner à la plage")
    choix: str = input("> ")

    if choix == "1":
        res = 13
    else:
        print("Choix invalide.")
        res = 17                  # on reste sur cette page

    return res
