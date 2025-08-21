import math

# ---- Calculatrice ---- 
def somme(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def puissance(a,b):
    return a**b

def racine_carree(a):
    return math.sqrt(a)

def affiche_resultat(operation, resultat):
    match operation:
        case "somme":
            print(f"La somme est {resultat}")
        case "soustraction":
            print(f"La différence est {resultat}")
        case "multiplication":
            print(f"Le produit est {resultat}")
        case "division":
            print(f"Le quotient est {resultat}")
        case "puissance":
            print(f"La puissance est {resultat}")
        case _:
            print(f"Le resultat est {resultat}")


print("Calculator activé")
affiche_resultat("somme",somme(1,2))
affiche_resultat("soustraction",soustraction(5,9))
affiche_resultat("multiplication",multiplication(4,5))
affiche_resultat("division",division(6,4))
affiche_resultat("puissance",puissance(4,5))
affiche_resultat("racine_carree",racine_carree(8))
