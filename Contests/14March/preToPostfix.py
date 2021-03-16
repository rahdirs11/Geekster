'''
Prefix to postfix conversion
'''


prefix = input()
postfix = str()

stack = []
operators = ['*', '+', '/', '%', '^', '-']
prefix = prefix[::-1]

for c in prefix:
    if c in operators:
        left, right = stack.pop(), stack.pop()
        stack.append((left + right + c))
    else:
        stack.append(c)
    # print(stack)

print(stack)
