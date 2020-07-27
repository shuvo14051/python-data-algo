class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        #head -> Shuvo ->  None>
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode  = currentNode.next




#firstNode.data = Shuvo, firstNode.next = None
firstNode = Node("Shuvo")
secondNode = Node("Labib")
thirdNode = Node("Sindid")

linkedList = LinkedList()

linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)

linkedList.printList()