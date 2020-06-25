/*
    Problem description
    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    Example:
    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

*/

/**
 * @param {number} n
 * @return {number}
 */

let memo = {};

let numTrees = (n) => {
    if (n === 0 || n === 1){
        return 1;
    }
    if (n in memo) {
        return memo[n];
    }
    let count = 0
    for (let i = 1; i <= n; i++){
        count += numTrees(i-1) * numTrees(n-i);
    }
    return count;
};