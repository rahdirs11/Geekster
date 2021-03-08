from sys import maxsize

def largestConsecutiveSum(arr: list) -> int:
    maxSum, currSum = -maxsize - 1, 0
    for num in arr:
        currSum += num
        maxSum = currSum if currSum > maxSum else maxSum
        currSum = 0 if currSum < 0 else currSum
    return maxSum

print(largestConsecutiveSum(list(map(int, input().split()))))
