"""
Fonctions annexes pour les combats.

Ces fonctions ne décident JAMAIS de la page suivante : elles retournent
une information (ici True / False) et c'est la page qui choisit la suite.

Pour les utiliser dans une page :
    from OUTILS.combat import combat_dragon
"""


attaques_loin: list = [{"nom": "attaque1-1", "degats": 1},{"nom": "attaque1-2", "degats": 2}] #liste de dictionnaire, chaque dictionnaire représente une attaque
attaques_proche: list = [{"nom": "attaque2-1", "degats": 1},{"nom": "attaque2-2", "degats": 2}]#liste de dictionnaire, chaque dictionnaire représente une attaque


def choisir_attaque(attaques: list) -> dict:
    '''
    affiche les attaques qu'on choisit et renvoies le dict associé
    '''
    compteur: int = 0 #initialise un compteur qui permet de mettre un numéro devant chaque attaque
    while compteur < len(attaques): # len(attaques) permet de récupérer le nombre exacte d'attaque dans nos 2 listes du début
        print(compteur + 1, "-", attaques[compteur]["nom"], "(", attaques[compteur]["degats"], "degats)") #on ajoute 1 au compteur pour que le premier numéro d'attaque ne soit pas 0
        compteur = compteur + 1
    numero: int = int(input("Votre attaque (numéro) : "))
    res = attaques[numero - 1] #on soustrait 1 au compteur pour retrouver le bon numéro (car on avait ajouté +1 juste avant)
    return res


def attaquer(monstre: dict, attaques: list, portee: str) -> None:
    '''
    on attaque en prenant en compte la faiblesse de l'adversaire (la portée)
    '''
    attaque: dict = choisir_attaque(attaques) #on récupère l'attaque choisit par le joueur
    degats: int = attaque["degats"] #on récupère la valeur de dégat de l'attaque qui est stocké dans nos 2 listes du débuts (attaques est une liste, on lui donne la valeur d'une des 2 listes dans la fonction tour_joueur)
    if monstre["portee_faible"] == portee:
        print( monstre["nom"], "est faible a cette distance.")
        degats = degats*2
    monstre["vie"] = monstre["vie"] - degats
    print("Votre", attaque["nom"], "inflige", degats, "dégats a", monstre["nom"], ". Il lui reste", monstre["vie"], "points de vie.")


def tour_joueur(gameState: dict, monstre: dict) -> None:
    '''
    tour du joueur, il chosiit quelle attaque faire
    '''
    if gameState["vie"] > 0:
        print("--- Que voulez vous faire ? ---")
        print("1 : Attaquer de loin")
        print("2 : Attaquer de près")
        choix: str = input("Votre choix :")
        if choix == "1":
            attaquer(monstre, attaques_loin, "loin") #donne les valeurs que la fonction attaquer va prendre, dans ce cas là elle prendra la liste d'attaque loin
        elif choix == "2":
            attaquer(monstre, attaques_proche, "proche")#donne les valeurs que la fonction attaquer va prendre, dans ce cas là elle prendra la liste d'attaque proche
        else:
            print("Choix inconnu, vous perdez votre tour !")


def tour_nevron(gameState: dict, monstre: dict) -> None:
    '''
    tour du monstre, il joue tout seul
    '''
    if monstre["vie"] > 0:
        gameState["vie"] = gameState["vie"] - monstre["force"]
        print(monstre["nom"], "vous attaque de", monstre["force"], "dégats. Il vous reste",
              gameState["vie"], "points de vie.")


def combat(gameState: dict, monstre: dict) -> bool:
    '''
    Combat générique entre le héros et un monstre.
    
        gameState : le dictionnaire du jeu (contient "vie" et "force" du héros)
        monstre   : un dictionnaire avec les clés "nom", "vie" et "force"
    
        Retourne True si le héros gagne, False s'il perd.
        Les points de vie du héros perdus pendant le combat sont retirés
        de gameState["vie"].
    '''
    res: bool = False
    while gameState["vie"] > 0 and monstre["vie"] > 0: #on regarde si le joueur et le monstre ont encore de la vie, sinon le combat s'arrête
        if gameState["vitesse"] >= monstre["vitesse"]:
            tour_joueur(gameState, monstre)
            tour_nevron(gameState, monstre)
        else:
            tour_nevron(gameState, monstre)
            tour_joueur(gameState, monstre)
    if gameState["vie"] > 0 and monstre["vie"] <= 0: #la condition s'éxécute quand le while n'est plus actif donc si le joueur n'a plus de vie alors le res reste égale à False, mais si c'est le monstre qui n'a plus de vie alors le res devient True
        res = True
    return res



def combat_nevron_classique(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron", "vie": 20, "force": 3, "vitesse": 5, "portee_faible": "proche"}
    res: bool = combat(gameState, monstre)
    return res

def combat_nevron_sentinelle(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron Sentinelle", "vie": 35, "force": 6, "vitesse": 10, "portee_faible": "loin"}
    res: bool = combat(gameState, monstre)
    return res

def combat_nevron_gardien(gameState: dict) -> bool:
    """Combat contre un névron (monstre). Retourne True si le héros gagne."""
    monstre: dict = {"nom": "Névron Gardien", "vie": 45, "force": 8, "vitesse": 15,"portee_faible": "proche"}
    res: bool = combat(gameState, monstre)
    return res