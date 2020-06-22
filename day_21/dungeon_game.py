"""
Problem Description:
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room
and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
"""


def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    solution = [[1] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # d_exist refers to "element down exist", r_exist refers to "element right exist"
            d_exist, r_exist = i + 1 < m, j + 1 < n
            if d_exist and r_exist:
                health_req = min(solution[i + 1][j], solution[i][j + 1]) - dungeon[i][j]
            elif d_exist:
                health_req = solution[i + 1][j] - dungeon[i][j]
            elif r_exist:
                health_req = solution[i][j + 1] - dungeon[i][j]
            else:
                health_req = 1 - dungeon[i][j]
            solution[i][j] = max(health_req, 1)
    return solution[0][0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(calculateMinimumHP(dungeon))
