def factorial(n):

    # basec case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


result = factorial(6)
print(result)
