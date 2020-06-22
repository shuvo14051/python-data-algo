def gcd(a,b):
    if a>b:
        c = a
        a = b
        b = c

    while b!=0:
        temp = a%b
        a = b
        b = temp

    return a


def lcm(a,b):
    return (a*b)//gcd(a,b)


print("Please input two integers:")
a, b = map(int, input().split())

l = lcm(12,18)
print(l)
