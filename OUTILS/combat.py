"""
Fonctions annexes pour les combats.

Ces fonctions ne décident JAMAIS de la page suivante : elles retournent
une information (ici True / False) et c'est la page qui choisit la suite.

Pour les utiliser dans une page :
    from OUTILS.combat import combat_dragon
"""


def combat(gameState: dict, monstre: dict) -> bool:
    """
    Combat générique entre le héros et un monstre.

    gameState : le dictionnaire du jeu (contient "vie" et "force" du héros)
    monstre   : un dictionnaire avec les clés "nom", "vie" et "force"

    Retourne True si le héros gagne, False s'il perd.
    Les points de vie du héros perdus pendant le combat sont retirés
    de gameState["vie"].
    """
    res: bool = False


    combat_fini: int = 2
    while combat_fini != 1 :
        if gameState["vitesse"] >= monstre["vitesse"]:
            monstre["vie"] = monstre["vie"] - gameState["force"]
            print("Vous avez mis", gameState["force"], "dégâts à", monstre["nom"], ". Il lui reste", monstre["vie"])
            if monstre["vie"] <= 0 :
                combat_fini = 1
                res = True
            else: 
                gameState["vie"] = gameState["vie"] - monstre["force"]
                print("Le monstre vous attaque de", monstre["force"], "dégâts. Il vous reste", gameState["vie"])
                if gameState["vie"] <= 0 :
                    combat_fini = 1
                    res = False
        else:
            gameState["vie"] = gameState["vie"] - monstre["force"]
            print("Le monstre vous attaque de", monstre["force"], "dégâts. Il vous reste", gameState["vie"])
            if gameState["vie"] <= 0 :
                combat_fini = 1
                res = False
            else: 
                monstre["vie"] = monstre["vie"] - gameState["force"]
                print("Vous avez mis", gameState["force"], "dégâts à", monstre["nom"], ". Il lui reste", monstre["vie"])
                if monstre["vie"] <= 0 :
                    combat_fini = 1
                    res = True

    return res


def combat_nevron_classique(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron", "vie": 10, "force": 2, "vitesse": 5}
    res: bool = combat(gameState, monstre)
    return res

def combat_nevron_sentinelle(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron Sentinelle", "vie": 20, "force": 5, "vitesse": 10}
    res: bool = combat(gameState, monstre)
    return res

def combat_nevron_gardien(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron Gardien", "vie": 50, "force": 10, "vitesse": 15}
    res: bool = combat(gameState, monstre)
    return res