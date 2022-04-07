"""
You are given a two-dimensional integer matrix of 1s and 0s. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water. You can assume that the edges of the matrix are surrounded by water.

Return the area of the largest island in matrix.
Leetcode: https://leetcode.com/problems/max-area-of-island/
"""
class Solution:
    
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num
    
    
    def maxAreaOfIsland(self, grid):
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
        return area_islands