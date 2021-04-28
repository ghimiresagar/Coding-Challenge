if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    socksDict = {}
    count = 0

    for x in ar:
        # complexity of n, loops through the whole dict
        # if x in socksDict:
        # complexity of 1, see if we can find a value for a key
        if socksDict.get(x):
            # if x exists in the dict, add to value
            socksDict[x] = socksDict[x] + 1
            # check if the value is now 2 so we can separate it as a pair
            if socksDict[x] != 0 and socksDict[x] % 2 == 0:
                count += 1
        else:
            # x doesn't exist, add a new dict item
            socksDict[x] = 1
    print(count)
