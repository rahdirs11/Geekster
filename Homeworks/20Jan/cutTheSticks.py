def cutTheSticks(arr: list) -> list:
    sticksCount = list()
    while len(arr) != 0:
        sticksCount.append(len(arr))
        smallestStick = min(arr)
        arr = list(map(lambda x: x - smallestStick, arr))
        arr = list(filter(lambda x: x, arr))
    return sticksCount


n = int(input())
sticks = list(map(int, input().split()))
if len(sticks) == n:
    print(cutTheSticks(sticks))
