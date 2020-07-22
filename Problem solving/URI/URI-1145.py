a, b = map(int, input().split())
x = 0
for i in range(1,b+1):
    print("%d " %i, end ='')
    x += 1
    if x == a:
        print()
        x = 0
