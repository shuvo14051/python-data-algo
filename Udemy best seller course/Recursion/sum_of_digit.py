def sum_digits(n):

    # base case
    if len(str(n)) == 1:
        return n

    else:
        return n % 10 + sum_digits(n//10)


result = sum_digits(4321)
print(result)
