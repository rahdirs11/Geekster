def pickingNumbers(a: list):
    frequency = {
        i: 0
        for i in range(1, 101)
    }

    for i in a:
        frequency[i] += 1
    

    maxLen = 0
    for i in range(2, 101):
        maxLen = max(frequency[i - 1] + frequency[i], maxLen)
    
    return maxLen


print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))