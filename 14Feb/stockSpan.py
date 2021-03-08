'''
For each value, find the number of elements that are <=
the value itself in the array
'''

def findSpan(arr):
    maxSpan = -1
    stack = []
    span = []
    i = 0
    while i < len(arr):
        while len(stack) != 0 and arr[stack[-1]] < arr[i]:
            stack.pop()
        # if len(stack) != 0:
        #     maxSpan = max(maxSpan, i - stack[-1])
        if len(stack) == 0:
            span.append(1)
        else:
            span.append(i - stack[-1])
        stack.append(i)
        i += 1
    # return maxSpan if maxSpan != -1 else 1
    return span

# print(findMax([1, 2, 3, 4, 5]))
print(findSpan([100, 80, 60, 70, 60, 75, 85]))