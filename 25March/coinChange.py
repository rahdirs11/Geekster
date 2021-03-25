def coins(target: int, array: list):
    strings = [0 for _ in range(target + 1)]
    strings[0] = 1
    for i in range(target + 1):
        for j in range(len(array)):
            if (i - array[j] >= 0):
                strings[i] += strings[i - arr[j]]
