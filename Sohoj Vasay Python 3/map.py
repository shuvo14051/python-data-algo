li = [1,2,3,4,5,6,7,8,9,10]

def cube(x):
    return x*x*x

li2 = map(cube, li)

print(list(li2))
