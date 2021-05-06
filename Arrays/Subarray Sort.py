def findPositionLeft(arr):
    smallest = float('inf')
    for x in range(len(arr) - 1):
        if arr[x] <= arr[x + 1]:
            # this is sorted and in place
            continue
        else:
            # not sorted and not in place, position of smaller number is x+1
            smallest = arr[x + 1]
            print(smallest)
            # find if there's any other number smaller than smallest
            for y in range(x + 1, len(arr) - 1):
                if smallest > arr[y]:
                    # if smaller change
                    smallest = arr[y]
        # break once the loop is over
        break
    # at this point we have the smallest number and it's index
    # find where this number should actually fit
    for x in range(len(arr)):
        if smallest < arr[x]:
            return x
    # if nthg's returned, return -1 as position
    return -1


def findPositionRight(arr):
    largest = -float('inf')
    for x in range(len(arr) - 1, -1, -1):
        if arr[x] >= arr[x - 1]:
            continue
        else:
            largest = arr[x - 1]
            for y in range(x, -1, -1):
                if largest < arr[y]:
                    largest = arr[y]
        break
    # find the index of where the largest unsorted number should fit
    for x in range(len(arr) - 1, -1, -1):
        if arr[x] < largest:
            return x
    return -1


def subarraySort(array):
    leftPosition = findPositionLeft(array)
    rightPosition = -1
    if leftPosition != -1:
        rightPosition = findPositionRight(array)
    return [leftPosition, rightPosition]

if __name__ == '__main__':
    print(subarraySort([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))