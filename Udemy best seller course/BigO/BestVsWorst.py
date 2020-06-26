"""
best case O(1)
worst case O(n)
"""
def matcher(li, match):
    for i in li:
        if i == match:
            return True
    return False

li = [1,2,3,4,5]
print(matcher(li,1))
