if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'wrld'

    # using loop
    dictTable = {x:0 for x in s2}
    flag = False
    for x in s1:
        if dictTable.get(x) == 0:
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")