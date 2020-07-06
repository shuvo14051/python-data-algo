"""
A
BB
CCC
DDDD
EEEEE
"""

for i in range(1,6):
    for j in range(i):
        print(chr(i+64),end='')
    print()