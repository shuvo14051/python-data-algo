"""
Pythonic way
li = list(map(int, input().split())) [:3]

maximum = max(li)

print(maximum)

"""

a,b,c = map(int, input("Enter three numbers:").split())

if a>=b and a>=c:
    greatest = a

elif b>=a and b>=c:
    greatest = b

else:
    greatest = c


print(greatest)
