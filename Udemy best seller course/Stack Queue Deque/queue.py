class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def allItems(self):
        print(self.items)


q = Queue()
q.enqueue(12)
q.enqueue(121)
q.enqueue(45)
print(q.isEmpty())
print(q.size())
print(q.dequeue())
