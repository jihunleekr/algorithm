import time

cache = [-1] * 30
for i in range(30):
    cache[i] = [-1] * 30


def bino2(n, r):
    if n == r or r == 0:
        return 1

    if cache[n][r] != -1:
        cache[n][r] = bino2(n - 1, r - 1) + bino2(n - 1, r)

    return cache[n][r]


t1 = time.time()
bino2(25, 12)
t2 = time.time()

print('time:', t2 - t1)