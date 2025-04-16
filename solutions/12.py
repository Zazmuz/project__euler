from helpers import prime_factors, mult
b = 0
s = 1
next = 2

while True:
    b = max(b, mult([i+1 for i in prime_factors(s).values()]))
    if b > 500: break
    s += next
    next += 1

print(s)