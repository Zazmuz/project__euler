n = 200000
is_prime = [True] * (n+1)
is_prime[0], is_prime[1] = False, False
p = 2

while p*p <= n:
    if is_prime[p]:
        for not_p in range(p*p, n+1, p):
            is_prime[not_p] = False
    p += 1

primes = [i for i in range(n+1) if is_prime[i]]

print(primes[10000])