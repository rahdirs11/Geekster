# from math import sqrt, ceil, floor

def squares(a: int, b: int) -> int:
    from math import sqrt, ceil
    count, start = 0, ceil(sqrt(a))
    while start * start <= b:
        count += 1
        start += 1

    return count


q = int(input())
while q >= 1:
    a, b = map(int, input().split())
    print(squares(a, b))
    q -= 1
