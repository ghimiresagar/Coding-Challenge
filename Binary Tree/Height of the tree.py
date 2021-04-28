class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.info = key

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.maxLevel = 0

    def create(self, val):
        # initialize the root if it doesn't exist
        if self.root is None:
            self.root = Node(val)
        else:
            # initialize the current position to be at root if the root already exists
            current = self.root
            # traverse so we can find an empty spot
            while True:
                # is the info less that current info
                if val < current.info:
                    # yes, so go to the left
                    # doesn't exist then this is the position to be
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    # since info can be greater go towards the right
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    # same info, we can just break
                    break

    def height(self, rootNode):
        leftHeight = 0
        rightHeight = 0
        if rootNode.left is not None:
            leftHeight = 1 + self.height(rootNode.left)
        if rootNode.right is not None:
            rightHeight = 1 + self.height(rootNode.right)
        return max(leftHeight, rightHeight)

    def leftView(self, rootNode, arr, level):
        if rootNode is None:
            return
        if level > self.maxLevel:
            arr.append(rootNode.info)
            self.maxLevel += 1

        self.leftView(rootNode.left, arr, level+1)
        self.leftView(rootNode.right, arr, level+1)

if __name__ == '__main__':
    bts = BinarySearchTree()
    bts.create(3)
    bts.create(5)
    bts.create(2)
    bts.create(1)
    bts.create(4)
    bts.create(6)
    bts.create(7)

    print(bts.height(bts.root))
    arr = []
    bts.leftView(bts.root, arr, 1)
    print(arr)
