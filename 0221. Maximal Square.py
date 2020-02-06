# dp[i][j] means the max side for a square 
# with its bottomright corner located at (i,j)
# dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
# time O(m*n), space O(m*n)

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        side = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                side = max(side, dp[i][j])
        
        return side*side



        
"""

Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""