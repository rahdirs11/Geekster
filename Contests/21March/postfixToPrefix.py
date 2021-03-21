postfix = input()
stack = []

for c in postfix:
    if c in ['+', '-', '*', '/', '%']:
        b, a = stack.pop(), stack.pop()
        newOperand = c + a + b
        stack.append(newOperand)
    else:
        stack.append(c)


print(stack[0])
