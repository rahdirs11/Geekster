'''
For a given number, find the count of binary numbers which have no adjacent
zeros.
'''

'''
For every number, 1 to the given number, calculate based on condition for
values ending with 1 and ending with 0

If a value ends with 0, then you can add another zero, so the count would be the previous
count for values ending with 1.

If a valule ends with 1, then we can add counts of ending with 1 and 0
'''


def binaryCount(number: int):
    dp = [[0 for _ in range(number + 1)] for _ in range(number + 1)]

    dp[0][0] = dp[1][0] = 1
    # first row will have all binary numbers ending with 0, without any adjacent zeros
    # second row will have all binary numbers ending with 1, without any adjacent zeros

    for i in range(1, number + 1):
        dp[0][i] = dp[1][i - 1]
        dp[1][i] = dp[1][i - 1] + dp[0][i - 1]

    return dp[0][-1] + dp[1][-1]
