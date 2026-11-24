from ASCII.ascii_dragon import ascii_dragon
from OUTILS.combat import combat_dragon


def page2(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    ascii_dragon()
    print("Un dragon surgit et vous barre la route !")

    resultat_combat: bool = combat_dragon(gameState)
    if resultat_combat == True:
        res = 0
    elif resultat_combat == False:
        res = -1

    return res
