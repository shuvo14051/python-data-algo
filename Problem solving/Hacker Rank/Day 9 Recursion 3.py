n = int(input())

def factorial(n):
    fact = 1
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(n)
print(result)