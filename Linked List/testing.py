# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    # this is to re order the nodes
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:  # if prev is node, node is the current head
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:  # this node is the tail
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert


    # position start with 1 and not 0
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        currentPosition = 1
        node = self.head
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                self.remove(current)
            current = current.next


    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


    def containsNodeWithValue(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def printll(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.setHead(Node(1))
    ll.setHead(Node(3))
    ll.setHead(Node(4))
    ll.setHead(Node(5))
    ll.setHead(Node(6))
    ll.setTail(Node(2))
    ll.insertAtPosition(4, Node(0))
    ll.printll()
    print()
    ll.removeNodesWithValue(1)

    ll.printll()