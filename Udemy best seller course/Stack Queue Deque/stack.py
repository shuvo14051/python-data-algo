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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def allItems(self):
        print(self.items)


s = Stack()

a = s.push(12)
b = s.push('as')
c = s.push(123)
d = s.push('name')

print(s.peak())
print(s.pop())
