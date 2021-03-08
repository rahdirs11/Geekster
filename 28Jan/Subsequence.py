def printSS(q, a):
    if len(q) == 0:
        print(a)
        return
    ch = q[0]
    printSS(q[1: ], ans + ch)
    print(a[1: ], ans)
