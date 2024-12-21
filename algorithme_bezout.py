# Déclaration de la fonction pour calculer les coefficients de Bézout
def bezout_coefficients(a, b):
    # Initialisation des restes et des coefficients
    old_r, r = a, b  # Les deux restes
    old_u, u = 1, 0  # Coefficients pour a
    old_v, v = 0, 1  # Coefficients pour b

    # Algorithme d'Euclide étendu
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_u, u = u, old_u - quotient * u
        old_v, v = v, old_v - quotient * v

    # Retourne le PGCD et les coefficients de Bézout
    return old_r, old_u, old_v

# Lecture des entrées utilisateur avec validation simple
a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))

if a1 > 0 and b1 > 0:  # Vérification que les deux nombres sont positifs
    # # Calcul du PGCD
    # pgcd = algorithme_euclid_pgcd(a1, b1)
    # print(f"PGCD({a1}, {b1}) = {pgcd}")

    # Calcul des coefficients de Bézout
    pgcd, u, v = bezout_coefficients(a1, b1)
    print(f"Les coefficients de Bézout sont : u = {u}, v = {v}")
    print(f"Vérification : {u} * {a1} + {v} * {b1} = {pgcd}")

elif a1 > 0 and b1 == 0 or a1 == 0 and b1 > 0:
    # Cas où l'un des nombres est 0
    if a1 > 0 and b1 == 0:
        # print(f"PGCD({a1}, {b1}) = {a1}")
        print(f"Les coefficients de Bézout sont : u = 1, v = 0")
    else:
        print(f"PGCD({a1}, {b1}) = {b1}")
        print(f"Les coefficients de Bézout sont : u = 0, v = 1")
else:
    print(f"Les deux nombres a et b sont nuls ou négatifs, a: {a1}, b: {b1}.")
