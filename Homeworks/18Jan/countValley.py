def countingValleys(steps: int, path: str) -> int:
    valley = mountain = 0
    numberOfValleys = 0
    for i, p in enumerate(path):
        if p == 'U':
            if not valley:
                mountain += 1
            else:
                valley -= 1
                if valley == 0:
                    numberOfValleys += 1
        elif p == 'D':
            if not mountain:
                valley += 1
            else:
                mountain -= 1
    return numberOfValleys


steps = int(input())
path = input()
print(countingValleys(steps, path))
