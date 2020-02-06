# use first row and first col to save "0", instead of using sets
# time O(m*n), in place, extra space O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        
        # check if first row and first column has zero
        first_row_has_zero = False
        first_col_has_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # search other area, and record zero to first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # update other area using first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        
        # update first row and column
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


# brute force, search all "0" and save their cols and rows in two sets
# time O(m*n), space O(m+n)
class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        if n == 0:
            return matrix
        
        cols = set()
        rows = set()
        # search all "0" and save their
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        # set the value of matrix with cols and rows to 0
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0



"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""
