# method 2: dp
# dp[i][j] means the number of ways going from (0, 0) to (i, j)
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
class Solution(object):
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
    
