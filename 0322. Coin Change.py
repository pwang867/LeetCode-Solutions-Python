# Solution 2: dynamic programming
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [-1]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] > -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount]



# Solution 1: recursion with memo, O(n)
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if not coins:
#             return -1
#         coins.sort(reverse=True)
#         print "coins =", coins
        
#         self.memo = {}  # {amount: num}
#         for coin in coins:
#             self.memo[coin] = 1

#         return self.helper(coins, amount)
        
#     def helper(self, coins, amount):
#         # return minimum number of coins to reach amount
#         if amount == 0:
#             return 0
#         if amount in self.memo:
#             return self.memo[amount]
#         if amount < coins[-1]:
#             return -1
        
#         ans = float("inf")
#         for coin in coins:
#             if coin < amount:
#                 temp = self.helper(coins, amount - coin)
#                 if -1 < temp < ans:
#                     ans = temp + 1
#                     # break
#         if ans == float("inf"):
#             ans = -1
#         self.memo[amount] = ans
#         return ans
    
