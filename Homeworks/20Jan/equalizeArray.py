def equalizeArray(arr: list) -> int:
    frequency = {}
    for a in arr:
        frequency[a] = frequency.get(a, 0) + 1

    mostCommon = max(frequency.values())
    return len(arr) - mostCommon

print(equalizeArray([int(x) for x in input().split()]))
