



// Definition for a binary tree node.
function TreeNode(val = 0, left =  null, right =  null) {
    this.val = (val)
    this.left = (left)
    this.right = (right)
}



/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (!root) return root;
    [root.left, root.right] = [invertTree(root.right), invertTree(root.left)]
    return root;
};