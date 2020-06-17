class Solution:
    def dfs(self, board, i, j, seen):
        if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]):
            return False
        if board[i][j] == "X" or (i, j) in seen:
            return True
        else:
            seen.add((i, j))

        return self.dfs(board, i + 1, j, seen) and self.dfs(board, i - 1, j, seen) and self.dfs(board, i, j + 1, seen) \
               and self.dfs(board, i, j - 1, seen)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "X":
                    continue
                seen = set()
                if self.dfs(board, i, j, seen):
                    for row, col in seen:
                        board[row][col] = "X"
        return board


n = Solution()
k = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"], ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
     ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"], ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
     ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
     ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
print(n.solve(k))

l = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
     ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
     ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
     ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
