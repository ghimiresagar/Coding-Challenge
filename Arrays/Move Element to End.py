if __name__ == '__main__':
    # O(n) time complexity and O(1) is space complexity

    def moveElementToEnd(array, toMove):
        # ending position of the array
        endPos = len(array) - 1
        # loop through the array and find the first toMove element
        for x in range(len(array)):
            if array[x] == toMove:
                for y in range(endPos, x - 1, -1):
                    if array[y] != toMove:
                        # we can move it
                        array[x] = array[y]
                        array[y] = toMove
                        endPos = y - 1
                        break
                    else:  # last element is also toMove element
                        # we can't move so we will decrement
                        continue

        return array

    print([2, 1, 2, 2, 2, 3, 4, 2])
    print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
