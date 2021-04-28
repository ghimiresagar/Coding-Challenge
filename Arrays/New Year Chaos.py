if __name__ == '__main__':
    # q = [2, 5, 1, 3, 4]
    p = [1, 2, 3, 4, 5, 6, 7, 8]
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    bribe = 0

    Q = [P-1 for P in q]

    for i, P in enumerate(Q):
        # i is the current position, P is the original position
        if P - i > 2:
            print("Too chaotic")
            break
