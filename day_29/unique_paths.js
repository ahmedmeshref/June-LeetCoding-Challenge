/*
Problem Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
*/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
let uniquePaths = function(m, n) {
    let grid = [],
        row = n - 1,
        col = m - 1;

    // create an (n*m) empty grid
    for (let _ = 0; _ <= row; _++){
        grid.push(new Array(m).fill(0))
    }

    // fill the grid
    for (let i = row; i >= 0; i--){
        for (let j = col; j >= 0; j--) {
            if (i === row || j === col) grid[i][j] = 1;
            else grid[i][j] = grid[i+1][j] + grid[i][j+1];
        }
    }
    return grid[0][0];
};

console.log(uniquePaths(7, 3))