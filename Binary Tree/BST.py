import math

if __name__ == '__main__':
    def binarySearch(array, target):
        # take the left number if odd number is given
        return BST(array, target, math.floor(len(array) / 2))


    def BST(arr, target, pos):
        if pos == 0 and arr[pos] != target or pos > len(arr):
            return -1
        if arr[pos] > target:
            # target is to the left
            return BST(arr, target, math.floor(pos / 2))
        else:
            # target is to the right
            return BST(arr, target, pos + math.floor(pos / 2))
        return pos