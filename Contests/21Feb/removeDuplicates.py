string = input()
stack = []

for c in string:
	if len(stack) == 0 or stack[-1] != c:
		stack.append(c)
	else:
		stack.pop()

print(''.join(stack))