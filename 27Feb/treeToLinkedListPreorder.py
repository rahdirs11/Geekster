def toLinkedList(root):
	if not root:
		return
	if root.left == None and root.right == None:
		return
	if root.left != None:

		toLinkedList(root.left)
		temp = node.right
		root.right = root.left
		node.left = None
		curr = root.right
		while curr.right != None:
			curr = curr.right
		# iterating 

		curr.right = temp
		toLinkedList(root.right)

	toLinkedList(root.right)
