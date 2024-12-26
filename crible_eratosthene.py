import math
def crible_Eratosthène(n):

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if is_prime[i]:
            for multiple in range(i*i, n+1, i):
                is_prime[multiple] = False

    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes

n=90
print(f"Les nombres premiers inférieurs à {n} sont: {crible_Eratosthène(n)}")