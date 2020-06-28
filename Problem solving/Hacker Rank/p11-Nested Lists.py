
ar = [[0 for j in range(2)] for i in range(5)]

marks = []

for i in range(5):
    for j in range(2):
        k = input()
        ar[i][j] = k


for i in ar:
    marks.append(float(i[1]))

print(marks)




