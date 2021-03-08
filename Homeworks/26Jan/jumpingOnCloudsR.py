def jumpingOnClouds(c, k):
    i, e = 0, 100
    while (i + k) % n != 0:
        e -= 1
        if c[(i + k) % n]:
            e -= 2
        i = (i + k) % n
    e -= 1

    return e if not c[0] else e - 2


n, k = map(int, input().split())
c = [int(x) for x in input().split()]

print(jumpingOnClouds(c, k))

