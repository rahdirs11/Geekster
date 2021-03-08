'''
Find the maximum and minimum value in a BST.
'''


def max(root):
    if root.right == None:
        print(root.val)

    max(root.right)


def min(root):
    if root.left == None:
        print(root.val)

    max(root.left)
