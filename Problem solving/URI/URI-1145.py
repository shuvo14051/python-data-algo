a, b = map(int, input().split())
x = 0
if a>b:
    a,b = b,a
# if (a > 1 and a < 20) and (b > a and b < 100000):
if (a > 1 and a < 20) and (b > a and b < 100000):

    for i in range(1, b + 1):
        print("%d " % i, end='')
        x += 1
        if x == a:
            print()
            x = 0
