# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5]
#     d = 2
#     newArr = arr.copy()
#     for x in range(0, len(arr)):
#         if x < d:
#             newArr[len(arr) - x - 1] = arr[x]
#         else:
#             newArr[x - d] = arr[x]
#     print(newArr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    d = 2
    newArr = []
    for x in range(d, len(arr)):
        newArr.append(arr[x])
    for x in range(0, d):
        newArr.append(arr[x])
    print(newArr)