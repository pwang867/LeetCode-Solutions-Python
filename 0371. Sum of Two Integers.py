class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # There is no integer limit in python, so we need a mask
        mask = 2**32-1
        # print(bin(a&mask), bin(b&mask))
        if b == 0:
            return a if a&(2**31) == 0 else -self.getSum(~a, 1)
        x = a^b
        carry = (a&b) << 1
        return self.getSum(x&mask, carry&mask)
    
