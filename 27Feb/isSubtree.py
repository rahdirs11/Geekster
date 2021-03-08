def isSubtree(root1, root2) -> bool:
	if root1 == root2 == None:
		return True
	if root1 == None or root2 == None:
		return False

	if root1.val == root2.val:
		return isSubtree(root1.left, root2.left) and isSubtree(root1.right, root2.right)



def traveseToNode(root, subtreeNode) -> bool:
	if root == None:
		return False

	if root.val == subtreeNode.val:
		return isSubtree(root, subtreeNode)
	else:
		return traverseToNode(root.left, subtreeNode) or traverseToNode(node.right, subtreeNode)

	# return False
