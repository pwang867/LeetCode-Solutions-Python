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
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        LIMIT = (2 ** 31 - 1) // 10
        res = 0
        while x > 0:
            if res > LIMIT:   # check overflow
                return 0
            if res == LIMIT:
                if (sign == 1 and x > 7) or (sign == -1 and x > 8):
                    return 0
            res = res * 10 + x % 10
            x //= 10
        return res * sign


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
        
        