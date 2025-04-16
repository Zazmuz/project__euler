from functools import reduce
from collections import Counter
divs = list(range(1,21))
factors = Counter()

def prime_factors(n):
    factor = 2
    used = []
    while factor <= n:
        while n % factor == 0:
            used.append(factor)
            n //= factor
        factor += 1
    used.append(n)
    return Counter(used)

for div in divs:
    factors = factors | prime_factors(div)

factors = [factor ** count for factor, count in factors.items()]

mult = lambda x, y: x*y
print(reduce(mult, factors))
