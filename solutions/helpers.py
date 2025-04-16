def mult(arr):
    from functools import reduce
    mult = lambda x, y: x*y
    return reduce(mult, arr)

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