if __name__ == '__main__':
    def sumOfBorderThree(arr, position):
        sumThree = 0
        for x in range(position, position+3):
            sumThree += arr[x]
        return sumThree

    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    sum = []
    flag = False
    bigSum = 0
    # this is the array position
    for outer in range(0, 4):
        # the is the element position
        for inner in range(0, 4):
            sumTop = sumOfBorderThree(arr[outer], inner)
            sumMiddle = arr[outer+1][inner+1]
            sumBottom = sumOfBorderThree(arr[outer+2], inner)
            smallSum = sumTop + sumMiddle + sumBottom
            sum.append(smallSum)
            # this is from the second hourglass onwards
            if flag and smallSum > bigSum:
                bigSum = smallSum
            # this is for the first, very first number
            if not flag:
                bigSum = smallSum
                flag = True
    # print(sum)
    print(bigSum)
