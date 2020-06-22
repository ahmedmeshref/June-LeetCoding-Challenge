/*
Problem Description:
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room
and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
*/


/**
 * @param {number[][]} dungeon
 * @return {number}
 */
let calculateMinimumHP = function (dungeon) {
    let m = dungeon.length,
        n = dungeon[0].length,
        solution = [],
        d_exist, r_exist, min_health;
    for (let _ = 0; _ < m; _++) solution.push(new Array(n).fill(1));
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            d_exist = i + 1 < m;
            r_exist = j + 1 < n;
            if (d_exist && r_exist) min_health = Math.min(solution[i][j + 1], solution[i + 1][j]) - dungeon[i][j];
            else if (d_exist) min_health = solution[i + 1][j] - dungeon[i][j];
            else if (r_exist) min_health = solution[i][j + 1] - dungeon[i][j];
            else min_health = 1 - dungeon[i][j];
            solution[i][j] = Math.max(min_health, 1);
        }
    }
    return solution[0][0];
};

let dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]];
console.log(calculateMinimumHP(dungeon));