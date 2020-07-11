# this is a complete pythonnic way
# print(a[::-1])
a = "Shuvo"
li = []
for i in a:
    li.append(i)

reverse = ''

for i  in range(len(li)-1,-1,-1):
    reverse += li[i]

print(reverse)

