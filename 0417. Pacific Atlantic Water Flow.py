# DFS, start from boundaries, time/space O(n)
# water flows along non-increasing path


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False]*n for _ in range(m)]   # visited matrix
        atlantic = [[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, i, 0, pacific)
            self.dfs(matrix, i, n-1, atlantic)
        for j in range(n):
            self.dfs(matrix, 0, j, pacific)
            self.dfs(matrix, m-1, j, atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
        
    def dfs(self, matrix, i, j, visited):
        if visited[i][j]:
            return
        visited[i][j] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(matrix) and 0 <= q < len(matrix[0]) and \
            matrix[i][j] <= matrix[p][q]:
                self.dfs(matrix, p, q, visited)


'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
