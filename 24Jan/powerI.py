def power(a: int, b: int):
    ans = 1
    while b > 0:
        if b % 2:
            ans *= a
            b -= 1
        else:
            a *= a
            b //= 2
    return ans


print(power(2, 0))