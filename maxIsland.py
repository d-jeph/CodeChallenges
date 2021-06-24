"""
You are given a two-dimensional integer matrix of 1s and 0s. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water. You can assume that the edges of the matrix are surrounded by water.

Return the area of the largest island in matrix.
"""
class Solution:
    def __init__(self):
        self.visited = []

    def solve(self, matrix):
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        max_island = 0
        for row in range(self.row_len):
            for col in range(self.col_len):
                if matrix[row][col] == 1:
                    self.total = 0
                    self.dfs(matrix, row, col)
                    max_island = max(max_island, self.total)
        return max_island


    def dfs(self, matrix, row, col):
        self.total += 1
        matrix[row][col] = 0
        if row - 1 >= 0 and matrix[row - 1][col] == 1:
            self.dfs(matrix, row - 1, col)
        if col - 1 >= 0 and matrix[row][col - 1] == 1:
            self.dfs(matrix, row, col - 1)
        if row + 1 < self.row_len and matrix[row + 1][col] == 1:
            self.dfs(matrix, row + 1, col)
        if col + 1 < self.col_len and matrix[row][col + 1] == 1:
            self.dfs(matrix, row, col + 1)