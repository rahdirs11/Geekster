n = int(input())

dp = [0 for _ in range(5 * 10 ** 5 + 1)]
i = 1
value, longest = 0, 0
while i <= n:
    seq, length = i, 1
    while seq != 1:
        if dp[seq]:
            length += dp[seq]
            break
        else:
            length += 1
            seq = seq // 2 if seq % 2 == 0 else 3 * seq - 1
    dp[i] = length
    i += 1

print(max(dp), dp.index(max(dp)))
