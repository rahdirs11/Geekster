def magicSquare(n=3):
    i, j = n // 2, n - 1
    ms = [[0 for i in range(n)] for j in range(n)]
    num = 1
    while num <= n ** 2:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        # print(i, j)
        if not ms[i][j]:
            ms[i][j] = num
            num += 1
        else:
            j -= 2
            i += 1
            continue

        i -= 1
        j += 1
    
    return ms


for row in magicSquare(int(input())):
    for col in row:
        print(col, end=" ")
    print()