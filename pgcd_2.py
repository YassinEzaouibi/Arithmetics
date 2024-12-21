a = int(input("Entrez la valeur du premier nombre (a+) : "))
b = int(input("Entrez la valeur du deuxième nombre (b+) : "))

if a > b :
    min = b
else :
    min = a

for i in range(1, min+1):
    if a % i == 0 and b % i == 0 :
        pgcd = i
print(f"hahow min {min} ou hahow min+1 {min}")
print(f"le pgcd de {a} et {b} c'est: {pgcd}")
print("le pgcd de ", a, " et ",b," c'est: ",pgcd,".")

