from OUTILS.combat import combat_nevron_classique

def page16(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous utilisez la corde.")

    if gameState["vent_fort"] == True:
        print("Le vent soufle trop fort, la corde casse !")
        res = -1
    else:
        print("Vous arrivez au sommet, en toute sécurité. Vous vous retrouvez face à un Névron (monstre).")


    resultat_combat: bool = combat_nevron_classique(gameState)
    if resultat_combat == True:
        print("Vous avez gagné !")
        res = 17
    elif resultat_combat == False:
        res = -1

    return res