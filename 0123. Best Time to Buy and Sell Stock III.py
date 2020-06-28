# at most two transactions


"""
# use the same method as #188. Best Time to Buy and Sell Stock IV

# method 3: a generalization method to k transactions, complexity O(n*k)

loc[i][j] = max(diff + glo[i-1][j-1], loc[i-1][j]+diff)
glo[i][j] = max(glo[i-1][j], loc[i][j])

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        k = 2
        loc = [0]*(k+1)
        glo = [0]*(k+1)
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                loc[j] = max(glo[j-1]+diff, loc[j]+diff)
                glo[j] = max(loc[j], glo[j])
        
        return glo[-1]

        
# method 2: O(n)        
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        
        # endProfit[i] means the max profit of one transaction in prices[:i+1]
        endProfit = [0] 
        minPrice = prices[0]
        for i, price in enumerate(prices[1:]):
            minPrice = min(minPrice, price)
            endProfit.append(max(endProfit[-1], price - minPrice))
        
        # startProfit[j] means the max profit of one transaction in prices[j:]
        startProfit = [0]*n
        maxPrice = prices[-1]
        for j in range(len(prices)-2, -1, -1):
            maxPrice = max(prices[j], maxPrice)
            startProfit[j] = max(startProfit[j+1], maxPrice - prices[j])
        
        profit = 0
        for i in range(n):
            profit = max(profit, endProfit[i] + startProfit[i])
        
        return profit
        

# method 1: divide and conquer O(n^2)
# divide the array into two pieces and calculate profit for each slice


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in range(len(prices)):
            profit = max(profit, 
                    self.oneSell(prices, 0, i-1) + self.oneSell(prices, i, n-1))
        
        return profit
            
    
    def oneSell(self, prices, left, right):
        if right - left < 1:
            return 0
        
        minPrice = prices[left]
        profit = 0
        for i in range(left, right+1):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i] - minPrice)
        
        return profit

    
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
