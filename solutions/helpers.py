def mult(arr):
    from functools import reduce
    mult = lambda x, y: x*y
    return reduce(mult, arr, 1)

def prime_factors(n):
    from collections import Counter
    factor=2
    used = []
    while factor <= n:
        while n % factor == 0:
            used.append(factor)
            n //= factor
        factor += 1
    if n != 1:
        used.append(n)
    return Counter(used)

def primes_n(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    p = 2

    while p*p <= n:
        if is_prime[p]:
            for not_p in range(p*p, n+1, p):
                is_prime[not_p] = False
        p += 1

    return [i for i in range(n+1) if is_prime[i]]

def digit_sum(n):
    return sum([int(x) for x in str(n)])

def factorial_to_n(n):
    l = [1, 1]
    for i in range(2, n+1):
        l.append(l[i-1] * i)
    return l