# 2D dp, time/space O(n^2)
# dp[i][j] means how much more can player 1 have than player 2 for piles[i:j+1]
# j - i + 1 is always even
# equation: dp[i][j] = max( min(dp[i+2][j]-piles[i+1], dp[i+1][j-1]-piles[j]) + piles[i], 
#                           min(dp[i][j-2]-piles[j-1], dp[i+1][j-1]-piles[i]) + piles[j] )
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
                    dp[i][j] = max( min(dp[i+2][j]-piles[i+1], dp[i+1][j-1]-piles[j]) + piles[i], 
                                   min(dp[i][j-2]-piles[j-1], dp[i+1][j-1]-piles[i]) + piles[j] )
        
        return dp[0][n-1] > 0

    
"""
Alex and Lee play a game with piles of stones.  
There are an even number of piles arranged in a row, 
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  
The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  
Each turn, a player takes the entire pile of stones 
from either the beginning or the end of the row.  
This continues until there are no more piles left, 
at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, 
return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
"""
