class Pair:
	def __init__(self):
		pass


def diameter(node) -> int:
	return diameterHelper(node).maxdiameter

def diameterHelper(node):
	if node == None:
		return Pair(0, 0)

	left = diameterHelper(node.left)
	right = diameterHelper(node.right)
	myDiameter = left.height + right.height + 1
	maxD = max(myDiameter, max(left.maxDiameter, right.maxDiameter))

	return Pair(max(left.height, right.height) + 1, maxD)