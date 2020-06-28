# minMax problem

# method 2: dp
# time O(n^3), space O(n^2)


class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[0]*(n+1) for _ in range(n+1)]
        # dp[i][i+1] must be zero, so length==1 is skipped
        for length in range(2, n+1):
            for i in range(1, n+2-length):
                j = i + length - 1
                dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1])
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        
        return dp[1][n]


# method 1: recursion with memo, time O(n^3), space O(n^2)


class Solution1(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.getMoneyAmountHelper(1, n)
    
    def getMoneyAmountHelper(self, low, high):
        if high <= low:
            return 0
        if high - low == 1:
            return low
        if high - low == 2:
            return low + 1
        
        if (low, high) in self.memo:
            return self.memo[(low, high)]
        
        min_money = float('inf')
        for num in range(low, high+1):
            min_money = min(min_money, 
                            num + max(self.getMoneyAmountHelper(low, num-1), 
                                      self.getMoneyAmountHelper(num+1, high)))
        
        self.memo[(low, high)] = min_money
        return min_money


"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. 
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.
"""
