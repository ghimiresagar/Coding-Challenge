if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    swaps = 0
    positionPointer = 0
    for x in range(0, len(arr)):
        # check if the swap is necessary
        if x+1 == arr[x]:
            positionPointer += 1
            continue
        # get the element position that has value equals to x+1
        swapPosition = arr.index(x+1)
        tempValue = arr[positionPointer]
        arr[positionPointer] = arr[swapPosition]
        arr[swapPosition] = tempValue
        positionPointer += 1
        swaps += 1
    print(swaps, arr)