# dp, time O(n), space O(n)
# loc[i] means the max profit if a stock is sold on day prices[i]
# glo[i] means the max profit during prices[:i+1] without restriction

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


    
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
