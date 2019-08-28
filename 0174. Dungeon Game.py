# dp, from Princess to Knight
# dp[i][j] means the minimum health a Knight needs 
# before entering room (i, j) to save Princess

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
        
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]  # with padding
        dp[-2][-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j])
        
        return dp[0][0]
        
        
