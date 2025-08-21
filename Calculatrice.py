# ---- Calculatrice ---- 
def somme(a,b):
    return a+b

def soustraction(a,b):
    return a-b


def affiche_resultat(operation, resultat):
    match operation:
        case "somme":
            print(f"La somme est {resultat}")
        case "soustraction":
            print(f"La différence est {resultat}")
        case _:
            print(f"Le resultat est {resultat}")


print("Calculator activé")
affiche_resultat("somme",somme(1,2))
