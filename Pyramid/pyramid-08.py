"""
EEEEE
DDDDD
CCCCC
BBBBB
AAAAA
"""

for i in range(5,0,-1):
    for j in range(5):
        print(chr(i+64), end='')

    print()
