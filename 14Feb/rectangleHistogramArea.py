def maxArea(arr):
    leftBoundary, rightBoundary = [-1], [-1]
    i = 1
    stack = []
    while i < len(arr):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            stack.pop()
        if len(stack) != 0:
            leftBoundary.append(stack[-1])
        else:
            leftBoundary.append(-1)
        stack.append(i)
        i += 1
    
    stack = []
    i = len(arr) - 2
    while i >= 0:
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            stack.pop()
        
        if len(stack) != 0:
            rightBoundary.insert(0, stack[-1])
        else:
            rightBoundary.insert(0, -1)
        i -= 1
    
    result = -1
    for i in range(len(arr)):
        area = arr[i] * (rightBoundary[i] - leftBoundary[i] - 1)
        result = max(result, area)
    
    return result
