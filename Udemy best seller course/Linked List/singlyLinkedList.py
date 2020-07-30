class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertAt(self, newNode, position):
        if position < 0 or position>self.listLength():
            print("Invalid Position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
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

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

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
firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(15)
fourthNode = Node(1212)

linkedList = LinkedList()

linkedList.insertEnd(firstNode)
linkedList.insertEnd(secondNode)
linkedList.insertAt(thirdNode, 1)
linkedList.deleteEnd()
linkedList.printList()