#!/bin/python3
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftToRight, rightToLeft = 0, 0
    i, j = 0, len(arr) - 1
    while i < len(arr) and j >= 0:
        # print(arr[i][i], arr[j][j])
        leftToRight += arr[i][i]
        rightToLeft += arr[i][j]
        i += 1
        j -= 1
    print(leftToRight, rightToLeft)
    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
