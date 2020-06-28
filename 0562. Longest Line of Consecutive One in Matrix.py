# time/space O(m*n), dp


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        m, n = len(M), len(M[0])
        dp = [[[0] * 4 for j in range(n)] for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                dp[i][j] = [1] * 4
                if j - 1 >= 0:
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j][1] = dp[i - 1][j - 1][1] + 1
                if i - 1 >= 0:
                    dp[i][j][2] = dp[i - 1][j][2] + 1
                if i - 1 >= 0 and j + 1 < n:
                    dp[i][j][3] = dp[i - 1][j + 1][3] + 1
                res = max(res, max(dp[i][j]))
        return res


"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""
