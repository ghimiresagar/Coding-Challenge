import math

if __name__ == '__main__':
    charToFind = 'a'
    s = 'aba'
    n = 10
    # take the length of the string s
    length = len(s)
    count = 0
    # see how many are in the given string
    for x in s:
        if x == 'a':
            count += 1
    if n % length == 0:
        count = count * (n / length)
    else:
        floorCount = math.floor(n / length)
        count = floorCount * count
        # find where we are at count
        positionN = floorCount * length
        remainingN = n - positionN
        for x in range(0, remainingN+1):
            if s[x] == 'a':
                count += 1
    print(int(count))