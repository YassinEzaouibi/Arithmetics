import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = 6
if is_prime(n):
    print(f"{n} est premier")
else:
    print(f"{n} n'est premier")
