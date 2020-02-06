# O(log(n)), we only need to count the total number of 5 as factors from 1 to n
# as there are much more 2 than 5 

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        denominator = 5
        while n >= denominator:
            ans += n/denominator
            denominator *= 5
        return ans

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""