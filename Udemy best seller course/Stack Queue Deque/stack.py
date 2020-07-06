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


s = Stack()
s.push(12)
s.push(1)
s.push(112)
s.push(312)
s.push(612)
s.push(412)


print(s.full_stack())
print(s.pop())
print(s.full_stack())


