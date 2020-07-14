def sum(*kwargs):
    sum = 0
    for i in kwargs:
        sum += i

    return sum
print(sum(1,2,3))