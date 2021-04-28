'''
    Find out if a pair exists in a given array that sums to a given number
'''

if __name__ == '__main__':
    arr = [6, 4, 1, 7, 5, 4, 3, 0]
    sumWanted = 21

    # convert the array into a dict first
    arrDict = {x:arr[x] for x in arr}

    # check if the sum for the number exist
    for x in arr:
        numNeeded = sumWanted - x
        if arrDict.get(numNeeded):
            print("Sum possible")
            break
