import random

def page7(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print("Vous avez accepter de jouer.")

    pile_ou_face: str = random.choice(["pile", "face"])[0] # choisi une valeur aléatoire entre "pile" et "face". Le [0] permet de retourner une chaine de caractère, sans le [0] random.choice renvoie la liste contenant le résultat du tirage

    print("1 - Pile   2 - Face")
    choix: str = input("> ")

    if choix == "1":
        if pile_ou_face == "pile":
            print("Vous avez gagné.")
            res = 8
        else:
            print("Vous avez perdu.")
            res = 9
    elif choix == "2":
        if pile_ou_face == "face":
            print("Vous avez gagné.")
            res = 8
        else:
            print("Vous avez perdu.")
            res = 9
    else:
        print("Choix invalide.")
        res = 7    

    return res
