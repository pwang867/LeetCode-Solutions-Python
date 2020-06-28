# time/space O(n)
# same as problem #67

import collections


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = collections.deque()
        
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            cur = carry
            if i >= 0:
                cur += int(num1[i])
            if j >= 0:
                cur += int(num2[j])
            
            carry = cur//10
            res.appendleft(str(cur%10))
            
            i -= 1
            j -= 1
        
        return ''.join(res)


"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
