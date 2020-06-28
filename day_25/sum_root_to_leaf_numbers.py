class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root: TreeNode):
    def preOrderTraversal(root, tot):
        if root:
            # if node if not a leaf
            if root.left or root.right:
                if root.left:
                    root.left.val = (root.val * 10) + root.left.val
                if root.right:
                    root.right.val = (root.val * 10) + root.right.val
            else:
                tot += root.val
            tot = preOrderTraversal(root.left, tot)
            tot = preOrderTraversal(root.right, tot)
        return tot
    return preOrderTraversal(root, 0)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print(sumNumbers(root))
