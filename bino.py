def bino(n, r):
    if n == r or r == 0:
        return 1
    return bino(n - 1, r - 1) + bino(n - 1, r)