def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

largest = 0
for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        prod = num1 * num2
        if is_palindrome(prod):
            largest = max(largest, prod)

print(largest)