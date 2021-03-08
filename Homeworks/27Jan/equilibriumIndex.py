# def equilibriumPoint(A, N):
#     if N == 1:
#         return N
#     point = 1
#     while point < N - 1:
#         if sum(A[: point]) == sum(A[point + 1: ]):
#             return point + 1
#         point += 1
#     return -1

# the above code is not optimized


def equilibriumPoint(A, N):
    if N == 1:
        return N
    totalSum = sum(A)
    leftSum = 0
    for i, a in enumerate(A):
        totalSum -= a
        if totalSum == leftSum:
            return i + 1
        leftSum += i

    return -1





n = int(input())
a = [int(x) for x in input().split()]

print(equilibriumPoint(a, n))