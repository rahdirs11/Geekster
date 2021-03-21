'''
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side. If there is no element present which satisfies the above condition consider (-1) for that postion.

Note:- Try to do in O(N) time complexity.
'''

stack = []
n = int(input())
numbers = [int(x) for x in input().split()]

for i, num in enumerate(numbers):
    if i == 0:
        print(-1, end=" ")
        stack.append(num)
        continue

    while len(stack) != 0 and stack[-1] > num:
        stack.pop()
    print(stack[-1] , end=" ")
    stack.append(num)
