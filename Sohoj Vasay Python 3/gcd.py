def gcd(a,b):
    if a>b:
        c = a
        a = b
        b = c
        #gcd(b,a) #this also works, it's a recursion. but i can't understand
    while b!=0:
        temp = a%b
        a = b
        b = temp

    return a


print("Enter two number:")
a,b = map(int, input().split())
gcd_cal = gcd(a,b)
print(gcd_cal)
