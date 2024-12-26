# Déclaration de la fonction pour calculer le PGCD
def algorithme_euclid_pgcd(a, b):
    if a > 0 and b == 0:
       return  a
    elif a == 0 and b > 0:
        return b
    elif b > 0 and a > 0:
        i = 0
        while b != 0:
            i = i + 1
            print(f"a = {a}, b = {b}, reste = {a % b}, iteration {i}")
            a, b = b, a % b
        return a
    else:
       return print("Les  2 nombres nuls ou négatifs ne sont pas valides.")
    # print(f"Calcul du PGCD de {a} et {b} :")

# Lecture des entrées utilisateur avec validation simple
a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))

print(f"PGCD({a1}, {b1}) = {algorithme_euclid_pgcd(a1, b1)}")