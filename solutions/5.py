from collections import Counter
from helpers import prime_factors, mult
divs = list(range(1,21))
factors = Counter()

for div in divs:
    factors = factors | prime_factors(div)

factors = [factor ** count for factor, count in factors.items()]

print(mult(factors))