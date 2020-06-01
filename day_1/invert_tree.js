/*
Invert a binary tree.

Example:

Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
*/

// Definition for a binary tree node.
function TreeNode(val = 0, left =  null, right =  null) {
    this.val = (val)
    this.left = (left)
    this.right = (right)
}


let invertTree = function(root) {
    if (!root) return root;
    [root.left, root.right] = [invertTree(root.right), invertTree(root.left)]
    return root;
};

