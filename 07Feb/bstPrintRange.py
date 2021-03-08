def printRange(root, l: int, r: int) -> None:
    if root == None:
        return

    if root.val > r:
        printRange(root.left, l, r)

    if root.val >= l and root.val <= r:
        printRange(root.left, l, r)
        print(root.val)
        printRange(root.right, l, r)

    if root.val < r:
        printRange(root.right, l, r)
