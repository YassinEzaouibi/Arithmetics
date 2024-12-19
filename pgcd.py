# Déclaration de la fonction pour calculer le PGCD
def euclid_gcd(a, b):
    i = 0
    # print(f"Calcul du PGCD de {a} et {b} :")
    while b != 0:
        i = i + 1
        print(f"a = {a}, b = {b}, reste = {a % b}, iteration {i}")
        a, b = b, a % b
    return a

# Lecture des entrées utilisateur avec validation simple
a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))

if a1 > 0 and b1 > 0:  # Vérification que les deux nombres sont positifs
    print(f"PGCD({a1}, {b1}) = {euclid_gcd(a1, b1)}")
else:
    print("Les nombres nuls ou négatifs ne sont pas valides.")
