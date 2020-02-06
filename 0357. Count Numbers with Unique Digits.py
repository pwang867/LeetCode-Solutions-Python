# dp, dp[i] means the the count of unique-digit-numbers 
# in the range of 10^(i-1) <= x < 10^(i)
# count of four-digit unique-digit numbers: 9*(9*8*7)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        dp = [0]*(n+1)
        dp[1] = 10   # length 1 and 2 are special due to leading zeros
        dp[2] = 81   
        for i in range(3, min(n+1, 11)):
            dp[i] = dp[i-1]*(11-i)
        
        return sum(dp)

"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""
