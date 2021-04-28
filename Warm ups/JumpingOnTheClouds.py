if __name__ == '__main__':
    arr = [0, 0, 1, 0, 0, 1, 0]
    jump = 0
    count = 0
    while count != len(arr):
        if count+2 < len(arr) and arr[count+2] != 1:
            count += 2
        elif count+1 < len(arr):
            count += 1
        else:
            break
        jump += 1
    print(jump)
