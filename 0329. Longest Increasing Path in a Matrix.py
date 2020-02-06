# similar to method 1, but use a dp matrix instead of a hashmap
# time/space O(m*n)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, dp)
        return max([max(row) for row in dp])
    
    def dfs(self, matrix, i, j, dp):
        if dp[i][j] > 0:
            return
        dp[i][j] = 1
        for v in [(1,0),(-1,0),(0,1),(0,-1)]:
            p, q = i+v[0], j+v[1]
            if 0 <= p < len(matrix) and 0 <= q < len(matrix[0]) and matrix[p][q] > matrix[i][j]:
                self.dfs(matrix, p, q, dp)
                dp[i][j] = max(dp[i][j], dp[p][q]+1)
        

# method 1: brute force, DFS with memo
# we don't need to record visited positions, 
# because we can only travel from small number to large number
# time O(m*n), space O(m*n) due to recursion depth
class Solution1(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        self.memo = {}   # memo[(i, j)] is the maximum length of increasing path starting from (i, j)
        
        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, self.longestPathHelper(matrix, i, j))
                
        return res
        
    def longestPathHelper(self, matrix, i, j):
        # return the max length of path starting from (i, j)
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        res = 1
        for v in [(0,1), (0,-1), (1,0), (-1,0)]:
            p, q = i + v[0], j + v[1]
            if p >= 0 and p < len(matrix) and q >= 0 and q < len(matrix[0]) \
                and matrix[p][q] > matrix[i][j]:
                res = max(res, 1 + self.longestPathHelper(matrix, p, q))
        
        self.memo[(i, j)] = res
        return res

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
