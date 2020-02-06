# method 3: dp, time O(m*n), space O(min(m, n))
# uniquePaths(m, n) == uniquePaths(n, m)
class Solution(object):
    def uniquePaths(self, m, n):
        if n > m:  # to make n the smaller one
            m, n = n, m
            
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[-1]
    

# method 2: dp, space O(m*n)
# dp[i][j] means the number of ways going from (0, 0) to (i, j)
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
class Solution2(object):
    def uniquePaths(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]
        

# method 1: recursion with memo
class Solution1(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.memo = {(m-1,n-1):1}
        return self.uniquePathsRecursion(m, n, 0, 0)
    
    def uniquePathsRecursion(self, m, n, i, j):
        # the number of ways going from (i, j) to (m-1, n-1)
        if i==m-1 and j==n-1:
            return 1
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        cnt = 0
        if i < m-1:
            cnt += self.uniquePathsRecursion(m, n, i+1, j)
        if j < n-1:
            cnt += self.uniquePathsRecursion(m, n, i, j+1)
        
        self.memo[(i,j)] = cnt
        return cnt
    
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
