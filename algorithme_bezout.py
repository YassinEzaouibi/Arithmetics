# #####
#
# def algorithme_bezout(a, b, pgcd):
#     a = 600
#     b = 124
#     r = 4
#     global u, v
#     ### pgcd = a*u+b*v la fonction 4 = 104_20*5
#
#
#     return
#
#
#
# # Déclaration de la fonction pour calculer le PGCD
# def algorithme_euclid_pgcd(a, b):
#     i = 0
#     # print(f"Calcul du PGCD de {a} et {b} :")
#     while b != 0:
#         i = i + 1
#         print(f"a = {a}, b = {b}, reste = {a % b}, iteration {i}")
#         a, b = b, a % b
#     return a
#
# # Lecture des entrées utilisateur avec validation simple
# a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
# b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))
#
# pgcd = algorithme_euclid_pgcd(a1, b1)
#
# if a1 > 0 and b1 > 0:  # Vérification que les deux nombres sont positifs
#     print(f"PGCD({a1}, {b1}) = {algorithme_euclid_pgcd(a1, b1)}")
# else:
#     print("Les nombres nuls ou négatifs ne sont pas valides.")

def bezout_fct(a,b):
    if b == 0:
        return 1,0
    else:
        u , v = bezout_fct(b , a % b)
        return v , u - (a//b)*v

def resoud_equation(a,b,c):
    u,v = bezout_fct(a,b)
    return "Les solutions de l'équation {}x + {}y = {} sont:\n({} + {}k , {} - {}k)".format(a,b,c,u,b,v,a)
