'''
Find the longest subsequence between the two given strings.
'''


def lcs(string1, string2):
    dp = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if string1[j - 1] == string2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


print(lcs("AGGTAB", "GXTXAYB"))
