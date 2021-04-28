import math

if __name__ == '__main__':
    def combinations(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n < 1:
            return 0

        return combinations(n-1) + combinations(n-2) + combinations(n-3)

    # number of steps
    n = 7
    total = 0
    print(combinations(n))