# method 2, smart method, add num by one, 
# then change num to binary form and remove the first bit
class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""
        return bin(num+1)[3:]


# method 1, determine the number of binary digits first
class Solution1(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""
        n = 1
        while num > 2**n - 2:
            n += 1
        length = n - 1
        k = num - (2**(n-1) - 2) - 1
        res = bin(k)[2:]
        return '0'*(length - len(res)) + res




"""
Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:



 

Example 1:

Input: num = 23
Output: "1000"
Example 2:

Input: num = 107
Output: "101100"
 

Constraints:

0 <= num <= 10^9
"""
