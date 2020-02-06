class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (bin(n).count('1') == 1)

class Solution2(object):  # remove the last set bit
    def isPowerOfTwo(self, n):
        return n > 0 and n&(n-1) == 0

class Solution1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:  # Don't forget n=0
            return False
        
        while n != 1:  # n=0 will make a timelimit error
            if n%2 != 0:
                return False
            else:
                n = n/2
                
        return True
    

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""
