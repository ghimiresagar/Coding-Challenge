if __name__ == '__main__':
    n = 5
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

    def perform_operation(originalArr, operationArr, tempMax):
        # take in the originalArr and perform the operation through the range
        for x in range(operationArr[0], operationArr[1]+1):
            originalArrPosition = x-1
            originalArr[originalArrPosition] += operationArr[2]
            if originalArr[originalArrPosition] > tempMax:
                tempMax = originalArr[originalArrPosition]
        return originalArr, tempMax

    # number of operations
    m = len(queries)
    # array of n 0s
    arr = n * [0]
    tempMax = 0
    for x in queries:
        arr, tempMax = perform_operation(arr, x, tempMax)
    print(arr, tempMax)


