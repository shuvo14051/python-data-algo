"""
Time complexity O(n^2)
"""

print("Enter a number:", end='')
n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        count += 1

print("N = {} --> Count = {} ".format(n,count))