prefix = input()
stack = []

for c in prefix[::-1]:
    if c in ['+', '-', '*', '/', '%']:
        stack.append(f'({stack.pop()}{c}{stack.pop()})')
    else:
        stack.append(c)

print(stack[-1])
