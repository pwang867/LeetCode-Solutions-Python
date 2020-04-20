# time O(n^3)


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        memo = {}
        return self.dfs(piles, 0, 1, memo)

    def dfs(self, piles, i, M, memo):
        if i == len(piles):
            return 0
        if (i, M) in memo:
            return memo[(i, M)]
        other = float('inf')
        for j in range(i, i + 2 * M):
            if j >= len(piles):
                break
            other = min(other, self.dfs(piles, j + 1, max(M, j - i + 1), memo))
        memo[(i, M)] = sum(piles[i:]) - other
        return memo[(i, M)]


"""
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, 
and each pile has a positive integer number of stones piles[i].  The objective of the game is to end 
with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  
Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. 
Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take 
all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""