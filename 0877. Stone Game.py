# 2D dp
# dp[i][j] means if the first layer can win for piles[i:j+1]
# equation: dp[i][j] = max( min(dp[i+2][j], dp[i+1][j-1]), 
#                        min(dp[i][j-2], dp[i+1][j-1]) )
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles:
            return False
        
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        
        for length in range(2, n+1, 2):
            for i in range(n-length+1):
                j = i + length - 1
                
                if length == 2:
                    
                    dp[i][j] = max(piles[i], piles[j]) - min(piles[i], piles[j])
                else:
                    dp[i][j] = max( min(dp[i+2][j], dp[i+1][j-1]) + piles[i], 
                                   min(dp[i][j-2], dp[i+1][j-1]) + piles[j] )
        
        return dp[0][n-1] > 0
    
