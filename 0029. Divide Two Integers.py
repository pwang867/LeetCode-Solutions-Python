# bit manipulation, find each bit for the result
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # bit manipulator, binary search
        # return divident/divisor
        if divisor == 0 or (dividend == -1<<31 and divisor == -1):
            return (1 << 31) - 1
        if (divisor > 0) ^ (dividend > 0):
            sign = -1
        else:
            sign = 1
        
        divisor = abs(divisor)
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
    
