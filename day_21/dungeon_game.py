def calculateMinimumHP(dungeon):
    n_row, n_col = len(dungeon), len(dungeon[0])
    solution = [[1] * n_col for _ in range(n_row)]
    for i in range(n_row - 1, -1, -1):
        for j in range(n_col - 1, -1, -1):
            # ed_exist refers to "element down exist", er_exist refers to "element right exist"
            ed_exist, er_exist = i + 1 < n_row, j + 1 < n_col
            if ed_exist and er_exist:
                health_req = min(solution[i + 1][j], solution[i][j + 1]) - dungeon[i][j]
            elif ed_exist:
                health_req = solution[i + 1][j] - dungeon[i][j]
            elif er_exist:
                health_req = solution[i][j + 1] - dungeon[i][j]
            else:
                health_req = 1 - dungeon[i][j]
            solution[i][j] = max(health_req, 1)
    return solution[0][0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(calculateMinimumHP(dungeon))
