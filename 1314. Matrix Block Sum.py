# time/space O(m*n)
# straightforward presum

class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        # get presum
        for i in range(m):
            for j in range(n):
                if i > 0:
                    mat[i][j] += mat[i-1][j]
                if j > 0:
                    mat[i][j] += mat[i][j-1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i-1][j-1]
        # produce results
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                p, q = [max(i-K, 0), max(j-K, 0)]
                x, y = [min(i+K, m-1), min(j+K, n-1)]
                cur = mat[x][y]
                if p > 0:
                    cur -= mat[p-1][y]
                if q > 0:
                    cur -= mat[x][q-1]
                if p > 0 and q > 0:
                    cur += mat[p-1][q-1]
                res[i][j] = cur
        return res


"""
Given a m * n matrix mat and an integer K, 
return a matrix answer where each answer[i][j] 
is the sum of all elements mat[r][c] for i - K <= r <= i + K, 
j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
Accepted
"""

