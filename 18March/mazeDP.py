def mazeStepsBU(destRow: int, destCol: int) -> int:
    dp = [[0 for _ in range(destCol + 1)] for _ in range(destRow + 1)]
    for i in range(destRow, -1, -1):
        for j in range(destCol, -1, -1):
            if i == destRow and j == destCol:
                dp[i][j] = 1
            else:
                if j == destCol:
                    dp[i][j] += dp[i + 1][j]
                elif i == destRow:
                    dp[i][j] += dp[i][j + 1]
                else:
                    dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
    return dp[0][0]

def mazeStepTD(destRow: int, destCol: int) -> int:
    dp = [[0 for _ in range(destCol + 1)] for _ in range(destRow + 1)]
    for i in range(0, destRow + 1):
        for j in range(0, destCol + 1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif i == destRow:
                    dp[i][j] += dp[i][j - 1]
                else:
                    dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
    return dp[destRow][destCol]


print(mazeStepsBU(2, 2))
