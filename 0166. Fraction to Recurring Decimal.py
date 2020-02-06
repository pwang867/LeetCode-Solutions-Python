# finding repeating pattern, use hashmap to record previous records

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator%denominator == 0:
            return str(numerator//denominator)
        
        # edge case: negative numbers
        if numerator*denominator > 0:    
            sign = 1
        else:
            sign = -1     
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = []
        if sign == -1:                
            res.append("-")
        
        res.extend([str(numerator//denominator), "."])
        i = len(res) - 1
        d = {}
        numerator = numerator%denominator
        while numerator > 0:
            numerator *= 10
            if numerator in d:
                start = d[numerator]  # the starting point of recurring
                return "".join(res[:start]) + "(" + "".join(res[start:]) + ")"
            res.append(str(numerator//denominator))
            i += 1
            d[numerator] = i
            numerator %= denominator
        return "".join(res)  # don't forget, here is for not recurring number


print(Solution().fractionToDecimal(1, 17))

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""
