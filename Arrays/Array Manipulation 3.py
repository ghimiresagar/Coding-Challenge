if __name__ == '__main__':
    n = 10
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    queries = [[1,5,3], [4,8,7], [6,9,1]]
    # queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

    def perform_operation(originalArr, operationArr):
        firstPos = operationArr[0]
        endPos = operationArr[1]
        value = operationArr[2]
        # add and subtract the starting and ending points to distinguish the beginning and the end
        originalArr[firstPos -1] += value
        # go up to 1 element extra so when finding the actual array at the end, this position neutralizes the rest
        originalArr[endPos] -= value
        print(originalArr)
        return originalArr

    # number of operations
    m = len(queries)
    # array of n 0s
    arr = (n+1) * [0]
    tempMax = 0
    for x in queries:
        arr = perform_operation(arr, x)
    # reorganize the array now
    for x in range(0, len(arr)-1):
        arr[x+1] = arr[x] + arr[x+1]
        if arr[x+1] > tempMax:
            tempMax = arr[x+1]
    print(arr, tempMax)


