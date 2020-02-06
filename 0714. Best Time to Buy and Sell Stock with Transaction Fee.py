# optimized from method 2, time O(n), space O(1)
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        loc = prices[1] - prices[0] - fee
        glo0 = 0
        glo1 = max(glo0, loc)
        for i in range(2, len(prices)):
            diff = prices[i] - prices[i-1]
            loc = max(diff - fee + glo0, loc + diff)
            glo0 = glo1
            glo1 = max(loc, glo1)
        return glo1

    
# time O(n), space O(n)
class Solution2(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        loc = [-float('inf')]*len(prices)
        glo = [-float('inf')]*len(prices)
        loc[1] = prices[1] - prices[0] - fee
        glo[0] = 0
        glo[1] = max(glo[0], loc[1])
        for i in range(2, len(prices)):
            diff = prices[i] - prices[i-1]
            loc[i] = max(diff - fee + glo[i-2], loc[i-1] + diff)
            glo[i] = max(loc[i], glo[i-1])
        return glo[-1]
    

# time O(n^2), space O(n), time limit exceeded
class Solution1(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        loc = [0]*len(prices)
        glo = [0]*len(prices)
        for i in range(1, len(prices)):
            for j in range(i):
                profit = prices[i] - prices[j] - fee
                if profit > 0:
                    if j == 0:
                        loc[i] = max(loc[i], profit)
                    else:
                        loc[i] = max(loc[i], profit + glo[j-1])
            glo[i] = max(loc[i], glo[i-1])
        return glo[-1]


"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
Accepted
"""
