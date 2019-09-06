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
            return 1   # (not 0 becuase 0 <= x < 10^0)
        if n == 1:
            return 10
        
        dp = [0]*(n+1)  # note that dp[0] = 0 (not 1)
        dp[1] = 10
        for i in range(2, min(n+1, 11)):
            dp[i] = 9
            j = 11-i
            while j < 10:
                dp[i] *= j
                j += 1
        
        return sum(dp)
    
