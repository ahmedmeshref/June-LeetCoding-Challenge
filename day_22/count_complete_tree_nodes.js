/*
    Problem Description: Given a complete binary tree, count the number of nodes.

    Input:
        1
       / \
      2   3
     / \  /
    4  5 6

    Output: 6
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function(root) {
    function inOrderTraversal(root, tot){
        if (root){
            tot = inOrderTraversal(root.left, tot);
            tot++;
            tot = inOrderTraversal(root.right, tot);
        }
        return tot;
    };
    return inOrderTraversal(root, 0);

};