n = 600851475143
largest = 0
for prime_factor in range(2, int(n**0.5) + 1):
    while n % prime_factor == 0:
        largest = max(largest, prime_factor)
        n //= prime_factor
    if n == 1:
        break
print(largest)