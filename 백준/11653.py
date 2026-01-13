n = int(input())
if n == 1:
    exit()

def prime_factors(n):
    if n == 1:
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            prime_factors(n // i)
            return

prime_factors(n)
