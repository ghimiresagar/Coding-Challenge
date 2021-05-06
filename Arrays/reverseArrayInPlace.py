if __name__ == '__main__':
    def reverseArray(arr):
        start = 0
        end = len(arr) - 1

        while start < end:
            if arr[start] < arr[end]:
                arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr


    print(reverseArray([1, 2, 2, 3, 6]))