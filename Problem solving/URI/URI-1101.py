while True:
    # a, b = map(int, input().split())
    a,b = [int(x) for x in input().split()] # another way to take input

    if a > b:
        a, b = b, a

    sum = 0
    for i in range(a, b + 1):
        sum += i

print(sum)
