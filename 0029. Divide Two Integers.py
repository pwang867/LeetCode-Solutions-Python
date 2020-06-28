# bit manipulation, find each bit for the result
# lots of edge case for overflow, handle them well

# edge case: divisor == 0, integer overflow
# edge case: dividend == -1<<31 and divisor == -1


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            raise ValueError("ZeroDivision")

        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        if divisor == MIN:
            if dividend == MIN:
                return 1
            else:
                return 0

        res = 0
        if dividend == MIN:
            if divisor == -1:
                return MAX
            elif divisor == 1:
                return MIN
            else:
                res = 1
                dividend += abs(divisor)

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            digit = 1
            copy = divisor
            # while divisor <= (MAX >> 1) and (divisor << 1) <= dividend:
            while dividend - divisor >= divisor:
                divisor <<= 1
                digit <<= 1
            res += digit
            dividend -= divisor
            divisor = copy

        return sign * res


# method 1 still has some problem, divisor = abs(divisor) might overflow
# method 2 solved this problem


class Solution1(object):
    def divide(self, dividend, divisor):  # return dividend//divisor
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -1<<31 and divisor == -1):
            return (1 << 31) - 1
        
        if (divisor > 0) ^ (dividend > 0):
            sign = -1
        else:
            sign = 1
        
        divisor = abs(divisor)   # might overflow
        dividend = abs(dividend)
        ans = 0
        
        copy = divisor
        while divisor <= dividend:  # wrong code: divisor < dividend
            factor = 1
            while (divisor << 1) < dividend:
                divisor = divisor << 1
                # wrong code factor << 1, which doesn't change factor
                factor = factor << 1  
            ans += factor
            dividend -= divisor
            divisor = copy
        
        ans = ans if sign == 1 else - ans
        
        return ans

"""
Given two integers dividend and divisor, 
divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment 
which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 231 − 1 when the division result overflows.
"""