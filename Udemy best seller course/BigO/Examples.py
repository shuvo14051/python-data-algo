def func_constant(li):
    print(li[0])


def func_linear(li):
    for i in li:
        print(i)

def func_quadratic(li):
    for i in li:
        for j in li:
            print(i,j)

li = [1, 2, 3]
func_quadratic(li)
