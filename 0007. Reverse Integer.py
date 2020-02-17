# edge case: interger overflow, negative numbers
# terminate while loop one digit earlier when reaching (2**31-1)//10
# 2**31 = 2147483648
# corner case: -1111111114, 9463847412

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        _max = 2**31 - 1  # max of 32-bit signed integer, 2147483647
        _min = -2**31
        if x > _max or x < _min:
            return 0
        
        # convert x to positive
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = -x
        
        res = 0
        while x > 0 and res < _max//10:  # check overflow !
            res = res*10 + (x%10)
            x = x//10
        
        if 0 == x:
            return res*sign
        
        # check overflow
        if res == _max//10:  
            # unnecessary: and ((sign > 0 and x <= 7) or (sign < 0 and x <= 8))
            # because the first digit of x must <= 2
            return (res*10 + x)*sign
        else:
            return 0
        
        
        

"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
"""
        
        