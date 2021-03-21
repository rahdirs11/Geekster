'''
Calculate the minimum cost it takes to reach from source to destination
'''
def minCost(board: list) -> int:
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0]) - 1, -1, -1):
            if i == len(board) - 1 and j == len(board[0]) - 1:
                dp[i][j] = board[i][j]
            else:
                if i == len(board) - 1:
                    dp[i][j] = board[i][j] + dp[i][j + 1]
                elif j == len(board) - 1:
                    dp[i][j] = board[i][j] + dp[i + 1][j]
                else:
                    dp[i][j] = board[i][j] + min(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


board = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

# print(board, len(board), len(board[0]), board[0], sep='\n\n')
print(minCost(board))
