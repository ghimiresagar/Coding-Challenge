import math

if __name__ == '__main__':
    arrayOne = [10, 0, 20, 25, 2000]
    arrayTwo = [1005, 1006, 1014, 1032, 1031]
    # 28, 26 == solution to this

    # variable to store the absolute smallest difference
    minDifference = math.inf
    resultArr = [0, 0]
    # sort the arrays in O(nlogn)
    arrayOne.sort()
    arrayTwo.sort()
    # [-1, 3, 5, 10, 20, 28]
    # [15, 17, 26, 134, 135]
    x = 0
    y = 0
    count = 0

    while x < len(arrayOne) and y < len(arrayTwo):
        print(arrayOne[x], arrayTwo[y], minDifference)
        if abs(arrayOne[x] - arrayTwo[y]) < minDifference:
            minDifference = abs(arrayOne[x] - arrayTwo[y])
            resultArr[0] = arrayOne[x]
            resultArr[1] = arrayTwo[y]
            print("inside :", resultArr[0], resultArr[1], minDifference)
        if arrayTwo[y] < arrayOne[x]:
            y += 1
        if arrayOne[x] < arrayTwo[y]:
            x += 1
        count += 1

    print(resultArr, count)