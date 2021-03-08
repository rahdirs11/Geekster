def preorder(root):	# node left right
	stack = []
	stack.append([root, 0])
	top = 0
	while len(stack) != 0:
		node = stack[top]
		if node[-1] == 0:
			print(node.val)
			stack[top][-1] += 1
		elif node[-1] == 1:
			if node[0].left != None:
				stack.append([node[0].left, 0])
			stack[top][-1] += 1
			top += 1 if node[0].left != None else 0
		elif node[-1] == 2:
			if node[0].right != None:
				stack.append([node[0].right, 0])
			stack[top][-1] += 1
			top += 1 if node[0].right != None else 0
		else:
			stack.pop()
			top -= 1


def postOrder(root): # left right node
	stack = []
	stack.append([root, 0])
	top = 0
	while len(stack) != 0:
		node = stack[top]
		if node[-1] == 0:
			if node[0].left != None:
				stack.append([node[0].left, 0])
			stack[top][-1] += 1
			top += 1 if node[0].left != None else 0
		elif node[-1] == 1:
			if node[0].right != None:
				stack.append([node[0].right, 0])
			stack[top][-1] += 1
			top += 1 if node[0].right != None else 0
		elif node[-1] == 2:
			print(node[0].val)
			stack.pop()
			top -= 1


