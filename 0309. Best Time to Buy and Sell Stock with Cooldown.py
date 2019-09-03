# dp, time O(n), space O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        loc = [0]*(n+1)  # with padding
        glo = [0]*(n+1)
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if i >= 2:
                loc[i+1] = max(loc[i]+diff, glo[i-2]+diff)
            else:
                loc[i+1] = loc[i]+diff
            glo[i+1] = max(loc[i+1], glo[i])
        
        return glo[-1]
    
