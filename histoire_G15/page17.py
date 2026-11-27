def page17(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous arrivez au sommet. Vous le reconnaissez car il était dessiné dans le carnet de votre soeur. En vous approchant un peu plus vous trouvez un des fragments du picto-mère. Une énigme se dresse devant vous.")
    
    print("énoncé enigme à faire")

    if gameState["culpabilité"] == False:
        print("indice sophie")

    reponse_enigme: str = input("Donner votre réponse\n> ")

    while (reponse_enigme != "reponse (chiffre)") or (gameState["vie"] != 0): #on éxécute la boucle tant que la réponse n'est pas bonne ou que le joueur a encore de la vie
        if reponse_enigme != "reponse (chiffre)":
            gameState["vie"] = gameState["vie"] - 1
            reponse_enigme: str = input("Donner votre réponse\n> ")
            print("Vous avez faux, ...", gameState["vie"])
        elif reponse_enigme == "reponse (chiffre)":
            print("Vous avez réussi l'énigme !")



    if gameState["vie"] == 0: #on vérifie que à la fin de l'énigme, le joueur a encore de la vie
        res = -1
    elif choix == "1":
        print("1 - Prendre le fragment du picto-mère et retourner à la plage")
        choix: str = input("> ")
        res = 13 #retourne à la plage
    else:
        print("Choix invalide.")
        res = 17                  # on reste sur cette page

    return res
