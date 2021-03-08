n = int(input())
heights = [int(x) for x in input().split()]

leftMin = [0 for _ in range(n)]
rightMin = [0 for _ in range(n)]

leftMin[0], rightMin[n - 1] = -1, n

stack = [0]
for i in range(1, n):
    while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
        stack.pop()
    
    if len(stack) == 0:
        leftMin[i] = -1
    else:
        leftMin[i] = stack[-1]
    stack.append(i)

stack = [n - 1]
for i in range(n - 2, -1, -1):
    while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
        stack.pop()
    
    if len(stack) == 0:
        rightMin[i] = n
    else:
        rightMin[i] = stack[-1]
        
    stack.append(i)
    
maxArea = 0
for i in range(n):
    area = heights[i] * (rightMin[i] - leftMin[i] - 1)
    maxArea = max(maxArea, area)

print(maxArea)
