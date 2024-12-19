def algorithme_euclid_pgcd_pour_ppcm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def algorithme_ppcm(a, b):
    ppcm = (a*b)//algorithme_euclid_pgcd_pour_ppcm(a,b)
    return ppcm

a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))

if a1 > 0 and b1 > 0:  # Vérification que les deux nombres sont positifs
    print(f"PGCD({a1}, {b1}) = {algorithme_euclid_pgcd_pour_ppcm(a1, b1)}")
    print(f"PPCM({a1}, {b1}) = {algorithme_ppcm(a1, b1)}")
else:
    print("Les nombres nuls ou négatifs ne sont pas valides.")