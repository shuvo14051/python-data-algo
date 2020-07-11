def Reverse(data):
    # this is like counting from 100 to 1 by taking one(-1)
    # step backward.
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


rev = Reverse('Shuvo')
for char in rev:
    print(char,end='')

print()

data = 'Shuvo'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))