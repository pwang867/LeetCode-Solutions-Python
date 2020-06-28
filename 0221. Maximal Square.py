# method 1, dp
# dp[i][j] means the max side for a square
# with its bottomright corner located at (i,j)
# dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
# time O(m*n), space O(m*n)


class Solution2(object):
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
                if matrix[i-1][j-1] == "0":   # easy to forget
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                side = max(side, dp[i][j])
        
        return side*side


# method 2, based on method 1, but optimize the space to O(n)
# rolling array


class Solution1(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        res = 0
        for i in range(m):
            dp[i % 2][0] = int(matrix[i][0])
            for j in range(1, n):
                if matrix[i][j] == "0":   # easy to forget
                    dp[i % 2][j] = 0
                else:
                    dp[i % 2][j] = min(dp[i % 2][j - 1], dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + 1
            res = max(res, max(dp[i % 2]))
        return res * res


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