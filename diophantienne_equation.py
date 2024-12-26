# def algorithme_euclid_pgcd_2(a, b):
#     i = 0
#     # print(f"Calcul du PGCD de {a} et {b} :")
#     while b != 0:
#         i = i + 1
#         # print(f"a = {a}, b = {b}, reste = {a % b}, iteration {i}")
#         # L'algorithme d'Euclide a = b * q + r
#         a, b = b, a % b
#     return a
#
# def diophantienne(a, b, n2):
#     d, u, v = algorithme_euclid_pgcd_2(a, b)
#
#     if n % d != 0:
#         return "There is no solution"
#
#     x0 = u * (n2 // d)
#     y0 = v * (n2 // d)
#
#     def solutionss(k):
#         x = x0 + k * (b // d)
#         y = y0 - k * (a // d)
#         return x, y
#
#     return solutionss
#
# a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
# b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))
# n = int(input("Entrez la valeur du n : "))
#
# # d = algorithme_euclid_pgcd_2(a1, b1)
# print("solutions: ")
# solutions = diophantienne(a1,b1,n)
# print(f"{solutions}")
#
def algorithme_euclid_pgcd_2(a, b):
    u0, v0, u1, v1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    return a, u0, v0

def diophantienne(a, b, n):
    d, u, v = algorithme_euclid_pgcd_2(a, b)

    if n % d != 0:
        return "There is no solution"

    x0 = u * (n // d)
    y0 = v * (n // d)

    def solutions(k):
        x = x0 + k * (b // d)
        y = y0 - k * (a // d)
        return x, y

    return solutions

# a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
# b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))
# n = int(input("Entrez la valeur du n : "))
#
# print("solutions: ")
# solutions = diophantienne(a1, b1, n)
# print(f"{solutions}")
a1 = int(input("Entrez la valeur du premier nombre (a+) : "))
b1 = int(input("Entrez la valeur du deuxième nombre (b+) : "))
n = int(input("Entrez la valeur du n : "))

print("solutions: ")
solutions = diophantienne(a1, b1, n)

# Example: Print solutions for k = 0, 1, 2
for k in range(3):
    x, y = solutions(k)
    print(f"Solution for k={k}: x={x}, y={y}")