ar = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
    for j in range(2):
        k = input()
        ar[i][j] = k

for i in range(5):
    for j in range(2):
        print(ar[i][j],end = ' ')
    print()

