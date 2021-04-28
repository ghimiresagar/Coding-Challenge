class Node:
    def __init__(self, val):
        self.info = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        # if no head, add head
        if not self.head:
            self.head = Node(val)
        else:
            # head is there find the last element and insert
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            # if next doesn't exist
            currentNode.next = Node(val)

    def __str__(self):
        currentNode = self.head
        arr = []
        while currentNode:
            arr.append(currentNode.info)
            currentNode = currentNode.next
        print(arr)

    def number(self, head):
        currentNode = head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    # function to shift the list head from algo expert
    # 12345 becomes 45123 with k = 2
    def headShift(self, head, k):
        # find the number of elements in the list
        count = self.number(head)
        newHeadPos = count - k
        # 5 elements, k = 2, means the head is gonna be after pos 3
        # traverse through the linked list upto where the new head is gonna be
        currentNode = head
        count = 1
        newHead = None
        while currentNode:
            if count == newHeadPos:
                # the next element is to be the new head
                newHead = currentNode.next
                currentNode.next = None
                break
            count += 1
            currentNode = currentNode.next
        print(newHead.info)

        currentNode = newHead
        while currentNode:
            if currentNode.next is None:
                currentNode.next = head
                self.head = newHead
                break
            currentNode = currentNode.next

if __name__ == '__main__':
    ls = LinkedList()
    ls.insert(1)
    ls.insert(2)
    ls.insert(3)
    ls.insert(4)
    ls.insert(5)

    ls.__str__()
    ls.headShift(ls.head, 1)
    ls.__str__()