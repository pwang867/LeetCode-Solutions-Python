# method 1, dynamic programming (dp)
# dp[i][j] means the number of ways to go from (0, 0) to (i, j)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i-1 >= 0:
                        dp[i][j] += dp[i-1][j]
                    if j-1 >= 0:
                        dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]
    
