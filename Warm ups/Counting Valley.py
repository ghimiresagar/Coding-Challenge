if __name__ == '__main__':
    valley = 'UDDDUDUUDU'
    countValley = 0
    level = 0

    for x in valley:
        if x == 'D':
            if level == 0:
                countValley += 1
            level -= 1
        else:
            level += 1
    print(countValley)