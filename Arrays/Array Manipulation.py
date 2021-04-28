if __name__ == '__main__':
    n = 10
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

    def perform_operation(originalArr, operationArr):
        # take in the originalArr and perform the operation through the range
        for x in range(operationArr[0], operationArr[1]+1):
            originalArrPosition = x-1
            originalArr[originalArrPosition] += operationArr[2]
        print(originalArr)
        return originalArr

    # number of operations
    m = len(queries)
    # array of n 0s
    arr = n * [0]
    min = 0
    for x in queries:
        arr = perform_operation(arr, x)
    for x in arr:
        if x > min:
            min = x
    print(arr, min)


