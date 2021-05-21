if __name__ == '__main__':
    # Tip: You can use the type(element) function to check whether an item
    # is a list or an integer.
    def productSum(array):
        return findProductSum(array, 0, 1)


    def findProductSum(arr, total, depth):
        for x in arr:
            if type(x) == int:
                total += x
            if type(x) != int:
                total += findProductSum(x, 0, depth + 1)
        return depth * total

    print(productSum([1, 2, [3], 4, 5]))