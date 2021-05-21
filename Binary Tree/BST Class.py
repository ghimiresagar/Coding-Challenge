# in algo expert, the BST class acts as a node
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            # node's value is greater, go towards the left if left exists
            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    current.left = BST(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = BST(value)
                    break

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def echo(self, value):
        print(self.value)

if __name__ == '__main__':
    bst = BST(5)
    bst.insert(4)
    bst.insert(6)
    bst.echo(bst.left)