if __name__ == '__main__':
    def recurse(arr, count, total, wait):
        if count == len(arr):
            return wait
        if count != 0:
            total = total + arr[count - 1]
        wait += total
        return recurse(arr, count + 1, total, wait)


    arr = [1, 2, 2, 3, 6]
    print(recurse(arr, 0, 0, 0))