a, b = 1, 1
s = 2
while len(str(b)) < 1000:
    s += 1
    a , b = b, a + b
print(s)