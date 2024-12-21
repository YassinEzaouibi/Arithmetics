# Déclaration de la fonction pour calculer le PGCD
def algorithme_euclid_pgcd(a, b):
    i = 0
    print(f"Calcul du PGCD de {a} et {b} :")
    while b != 0:
        i = i + 1
        print(f"a = {a}, b = {b}, reste = {a % b}, iteration {i}")
        # L'algorithme d'Euclide a = b * q + r
        a, b = b, a % b
    return a
try:
    # Lecture des entrées utilisateur avec validation simple
    a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
    b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))
except ValueError:
    print("Veuillez entrer des entiers valides.")
    exit()

if a1 > 0 and b1 > 0:  # Vérification que les deux nombres sont positifs
    print(f"PGCD({a1}, {b1}) = {algorithme_euclid_pgcd(a1, b1)}")
elif a1 > 0 and b1 == 0 or a1 == 0 and b1 > 0:
    if a1 > 0 and b1 == 0:
        print(f"PGCD({a1}, {b1}) = {a1}")
    else:
        print(f"PGCD({a1}, {b1}) = {b1}")
else:
    print(f"Les deux nombres a et b sont nuls ou négatifs, a: {a1}, b: {b1}.")