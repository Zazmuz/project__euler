def hailstone(n):
    og_n = n
    s = 1
    while n != 1:        
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        
        s += 1
    return s, og_n

maxx = (0,0)
for i in range(1, 1000000):
    maxx = max(maxx, hailstone(i))
print(maxx)