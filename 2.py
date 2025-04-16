a, b = 1, 2
s = a+b
while a+b < int(4e6):
    a, b = b, a+b
    s += b if b%2 == 0 else 0
print(s)