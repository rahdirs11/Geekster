'''
Swap the rigth and left nodes of every node
'''


def swapChildren(root):
	if root == None:
		return

	left = swapChildren(root.left)
	right swapChildren(root.right)

	root.left = right
	root.right = left

	return root

