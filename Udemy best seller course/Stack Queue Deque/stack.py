# Completed implementation of a stack ADT

#In this way of implementation we are adding from right to left
# the left most item is added first
# right most item is popped first
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items.pop(len(self.items) - 1)

    def beneath(self):
        return self.items.pop(0)

    def full_stack(self):
        return self.items

    def size(self):
        return len(self.items)


"""
#In this way of implementation we are adding from left to right
# the right most item is added first
# the left most item is popped first

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peak(self):
        return self.items.pop(len(self.items) - 1)

    def beneath(self):
        return self.items.pop(0)

    def full_stack(self):
        return self.items

    def size(self):
        return len(self.items)
"""

s = Stack()
s.push(12)
s.push(1)
s.push(11)


print(s.full_stack())
print(s.pop())
print(s.full_stack())





