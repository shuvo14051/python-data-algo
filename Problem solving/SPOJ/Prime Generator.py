test = int(input())
for i in range(test):
    a, b = map(int, input().split())

    for n in range(a, b+1):
        count = 0
        if n == 1:
            continue
        for j in range(2, (n//2)+1):
            if n % j == 0:
                count = count+1
        if count == 0:
            print(n)
