# in this solution, dp[i][j] means the counts for last time is dice i with frequency j

# this solution can be further improved by using deque, dp = {1: deque([]), 2: deque([]), ...}
# for every roll, insert a number into the beginning of the deque(), 
# which is frequency 1, and pop the deque if it is more than rollMax
# and we only need to maintain one dp
# the time complexity will be O(n) even without constraint 1 <= rollMax[i] <= 15

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        LIMIT = 10**9 + 7
        N = max(rollMax)  # max allowed frequence
        dp1 = [[0 for j in range(N+1)] for i in range(7)]
        for i in range(1, 7):
            if rollMax[i-1] >= 1:
                dp1[i][1] = 1
        
        for time in range(2, n+1):
            dp2 = [[0 for j in range(N+1)] for i in range(7)]
            for i in range(1, 7):
                total = sum(dp1[i])  
                for temp in range(1, 7):  # next time different dice
                    if temp != i and rollMax[temp-1] >= 1:
                        dp2[temp][1] += total
                for j in range(1, N+1):   # next time is still self
                    if dp1[i][j] == 0:
                        continue
                    if j + 1 <= rollMax[i-1]:                       
                        dp2[i][j+1] += dp1[i][j]
                        dp2[i][j+1] %= LIMIT
            dp1 = dp2
        
        return sum([sum(row)%LIMIT for row in dp1])%LIMIT



"""
A die simulator generates a random number from 1 to 6 for each roll. 
You introduced a constraint to the generator such that it cannot roll the 
number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, 
return the number of distinct sequences that 
can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs 
from each other. Since the answer may be too large, return it modulo 10^9 + 7.


Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
"""
