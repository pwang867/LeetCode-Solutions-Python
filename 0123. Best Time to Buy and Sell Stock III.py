# solution 2: use the same method as #188. Best Time to Buy and Sell Stock IV
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # method 3: a generazitation method to k transactions, complexity O(n*k)
        k = 2
        loc = [0]*(k+1)
        glo = [0]*(k+1)
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                loc[j] = max(glo[j-1], glo[j-1]+diff, loc[j]+diff)
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
    
