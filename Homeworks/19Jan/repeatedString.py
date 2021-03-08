from math import ceil

def repeatedString(s: str, n: int):
    length = len(s)
    reps = ceil(n / length)
    aCount = s.count('a') * (reps - 1)
    if not n % length:
        aCount += s.count('a')
    else:
        aCount += s[: n % length].count('a')
    return aCount

if __name__ == '__main__':
    s, n = input(), int(input())
    print(repeatedString(s, n))
