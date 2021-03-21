def climbDownDP(n: int, dp: dict={}) -> int:
    if n in dp:
        return dp[n]

    if n < 0:
        return 0

    if n == 0:
        return 1

    # minus1, minus2, minus3 = climbDownDP(n - 1, dp), climbDownDP(n -  2, dp), climbDownDP(n - 3, dp)
    # dp[n] = minus1 + minus2 + minus3
    dp[n] = climbDownDP(n - 1, dp) + climbDownDP(n -  2, dp) + climbDownDP(n - 3, dp)
    return dp[n]

def climbDown(n: int) -> int:
    if n < 0:
        return 0

    if n == 0:
        return 1

    return climbDown(n - 1) + climbDown(n - 2) + climbDown(n - 3)


def climbDownTab(n: int):
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2


if __name__ == '__main__':
    n = int(input())
    print(climbDownDP(n, {}))
    print(climbDown(n))
