def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("=== CRÉATION DU PERSONNAGE ===")
    nom: str = input("Quel est votre nom ? ")
    gameState: dict = {
        "nom": nom,
        "force": 10,
        "vie": 15,
        "vitesse": 10,
        "culpabilité": False,
        "vent_fort": False,
        "inventaire": [],
    }
    print(f"Bienvenue, {nom} ! Force : {gameState['force']}, Vie : {gameState['vie']}\n")
    return gameState
