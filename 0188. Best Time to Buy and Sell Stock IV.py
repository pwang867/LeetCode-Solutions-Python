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


    

"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""
