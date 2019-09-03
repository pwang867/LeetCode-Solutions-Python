
# method 2: dp based on method 1, but saves memory
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # k = min(k, (len(prices))//2), # this will still cause TLE
        # special case, when k is more than we need, it become Stock II
        if k > len(prices)//2:
            profit = 0
            for i in range(1, len(prices)):
                profit += max(0, prices[i]-prices[i-1])
            return profit
        
        loc = [0]*(k+1)  # local
        glo = [0]*(k+1)  # global
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                loc[j] = max(glo[j-1], glo[j-1]+diff, loc[j]+diff)
                glo[j] = max(glo[j], loc[j])
        
        return glo[-1]
    


# method 1, memory limit exceeded, but the dp equation is explained the best
class Solution1(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k = min(k,len(prices)-1)
        
        loc = [[0]*(k+1) for _ in range(len(prices))]  # local
        glo = [[0]*(k+1) for _ in range(len(prices))]  # global
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                loc[i][j] = max(glo[i-1][j-1], glo[i-1][j-1]+diff, 
                                loc[i-1][j]+diff)
                glo[i][j] = max(glo[i-1][j], loc[i][j])
        
        return glo[-1][-1]
    
