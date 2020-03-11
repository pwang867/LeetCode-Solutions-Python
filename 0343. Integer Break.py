# n will be broken into only 2 and 3
# if factor >= 4, then we can split factor to 2 and (factor-2) and always have 2*(factor-2) > factor
# 2*2*2 < 3*3, so we will have no more than three 2's
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 3**(n//3-1)*4
        if n % 3 == 2:
            return 3**(n//3)*2

        
"""
Given a positive integer n, break it into the sum of at least two positive 
integers and maximize the product of those integers. 
Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
