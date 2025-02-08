pws = [i**5 for i in range(10)]
s = 0
for i in range(10, 3_000_001):
    s += i if sum([pws[int(x)] for x in str(i)]) == i else 0
print(s)