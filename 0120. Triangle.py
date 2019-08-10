# use dynamic programming, bottom up
# space O(n) if original data can't be overwritten
# time O(n^2), where n is the length of row
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return []
        
        dp = triangle[-1]
        
        for row in range(len(triangle)-2, -1, -1):  # bottom up
            for i, num in enumerate(triangle[row]):
                dp[i] = num + min(dp[i], dp[i+1])
        
        return dp[0]
    
