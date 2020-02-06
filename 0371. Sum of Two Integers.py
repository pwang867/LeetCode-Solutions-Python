class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # There is no integer limit in python, so we need a mask
        mask = 2**32-1
        if b == 0:
            return a if a&(2**31) == 0 else -self.getSum(~a, 1)  
        # python don't recognize "0b10000000000000000000000000000000" as a negative number
        x = a^b
        carry = (a&b) << 1
        return self.getSum(x&mask, carry&mask)


"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""
