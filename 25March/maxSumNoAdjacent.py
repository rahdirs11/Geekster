def maxSum(array: list):
    dp = [[0 for _ in range(len(array))] for _ in range(len(array))]
    # first row is exclude, second is include
    for i, a in enumerate(array):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
        dp[1][i] = a + dp[0][i - 1]
    return max(dp[0][-1], dp[1][-1])


def maxSumNoArray(array: list):
    include, exclude = array[0], 0
    for i in array[1: ]:
        temp = max(include, exclude)
        include = i + exclude
        exclude = temp

    return max(include, exclude)



print(maxSum([5, 6, 10, 100, 10, 5]))
print(maxSumNoArray([5, 6, 10, 100, 10, 5]))
