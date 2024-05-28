"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, so an island is a group of 1s 
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

# Solution

"""
We can traverse the matrix linearly to find islands. Whenever we find a cell with the value '1' (i.e., land),
we have found an island. Using that cell as the root node, we will perform a Depth First Search (DFS) to find all of its connected land cells. 
During our DFS we will find and mark all the horizontally and vertically connected land cells. 

"""

class Solution:
    def countIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for row in range(rows):
            for col in range(cols):
                if(matrix[row][col]==1): # only if the cell is a land we have found an island
                    totalIslands += 1
                    self.mark_current_island_dfs(matrix, row, col) #visit and mark all adjacent lands using DFS
        
        return totalIslands


    def mark_current_island_dfs(self, matrix, i, j):
        if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])):
            return #return, if cell is out of bound
        
        if (matrix[i][j]==0 or matrix[i][j]==2):
            return  # return, if it is a water cell or cell is already visited

        matrix[i][j] = 2  # mark the cell visited by making it a 2

        # recursively visit all adjacent cells - horizontally and vertically
        self.mark_current_island_dfs(matrix, i - 1, j)  # up
        self.mark_current_island_dfs(matrix, i + 1, j)  # down
        self.mark_current_island_dfs(matrix, i, j - 1)  # left
        self.mark_current_island_dfs(matrix, i, j + 1)  # right



# test solution

test_matrix1 = [[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
test_matrix2 = [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
test_matrix3 = [[1, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1],[1, 1, 0, 0, 1]]

def test_solution():
  sol = Solution()
  assert sol.countIslands(test_matrix1) == 1 
  assert sol.countIslands(test_matrix2) == 3
  assert sol.countIslands(test_matrix3) == 4



test_solution()






