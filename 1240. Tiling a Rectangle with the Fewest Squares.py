# http://int-e.eu/~bf3/squares/

# brute force
class Solution:
    def tilingRectangle(self, n, m):
        self.n = n
        self.m = m
        board = [[0] * n for _ in range(m)]
        self.res = float('inf')
        self.dfs(board, 0)
        return self.res
    
    def dfs(self, board, count):
        if count >= self.res:
            return
        i, j = self.find_next(board)
        if i == -1 and j == -1:
            self.res = min(self.res, count)
            return
        max_length = self.find_max_length(board, i, j)
        for k in range(1, max_length + 1)[::-1]:
            self.assign(board, i, j, k, 1)
            self.dfs(board, count + 1)
            self.assign(board, i, j, k, 0)
    
    def assign(self, board, i, j, length, val):
        for row in range(i, i + length):
            for col in range(j, j + length):
                board[row][col] = val

    def find_max_length(self, board, i, j):
        max_length = 1
        while i + max_length -1 < self.m and j + max_length - 1 < self.n:
            for row in range(i, i + max_length):
                if board[row][j + max_length - 1] != 0:
                    return max_length - 1
            for col in range(j, j + max_length):
                if board[i + max_length - 1][col] != 0:
                    return max_length - 1
            max_length += 1
        return max_length - 1
        
    def find_next(self, board):
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 0:
                    return i, j
        return -1, -1
 
   
"""
Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

 

Example 1:



Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:



Input: n = 5, m = 8
Output: 5
Example 3:



Input: n = 11, m = 13
Output: 6
 

Constraints:

1 <= n <= 13
1 <= m <= 13
"""
