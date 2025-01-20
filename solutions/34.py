from helpers import factorial_to_n
facs = factorial_to_n(10)
s = 0
for i in range(10, 3_000_001):
    s += i if sum([facs[int(x)] for x in str(i)]) == i else 0
print(s)