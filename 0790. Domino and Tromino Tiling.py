"""
dp[i] = 

dp[i-1]  + 
....X
....X

dp[i-2]  +
....XX
....YY

dp[i-3]*2  + 
...YXX
...YYX

...YYX
...YXX

dp[i-4]*2 + ...
...YZZX
...YYXX

...YYXX
...YZZX

"""

# method 2: simplified from method 1, dp
# dp[i] = dp[i-1] + dp[i-2] + (dp[i-3] + ... + dp[0])*2
# can be simplified to dp[i] = 2*dp[i-1] + dp[i-3]
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 1:
            return 0
        if N < 3:
            return N
        
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, N+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
            dp[i] %= 10**9+7
        
        return dp[N]



# method 1: dp
class Solution1(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return 1
        
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
            j = i - 3
            while j >= 0: # tromino-(domino)^(2*m)-trimino
                dp[i] += 2*dp[j]
                j -= 2
            j = i -4
            while j >= 0:  # tromino-(domino)^(2*m+1)-trimino
                dp[i] += 2*dp[j]
                j -= 2
            dp[i] %= 10**9+7
        
        return dp[N]
    
        
"""
790. Domino and Tromino Tiling
Medium

326

171

Add to List

Share
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
"""
