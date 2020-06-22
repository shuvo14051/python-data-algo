def cumulative_sum(n):

    if n == 0:
        return 0

    else:
        return n + cumulative_sum(n-1)


result = cumulative_sum(4)
print(result)
