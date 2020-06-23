"""
    Problem Description: Given a complete binary tree, count the number of nodes.

    Input:
        1
       / \
      2   3
     / \  /
    4  5 6

    Output: 6
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode, tot):
        if root:
            tot = self.countNodes(root.left, tot)
            tot += 1
            tot = self.countNodes(root.right, tot)
        return tot


# this part is for testing only and not part of the leetcode solution
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
tree = Solution()
print(tree.countNodes(root, 0))
