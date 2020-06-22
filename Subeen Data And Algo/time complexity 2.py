"""
Time complexity O(n^2+n)
the value of n^2 is significantly greater than n.
so the Time complexity O(n^2)
"""

print("Enter a number:", end='')
n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        count += 1


for i in range(n):
    count += 1

print("N = {} --> Count = {} ".format(n,count))