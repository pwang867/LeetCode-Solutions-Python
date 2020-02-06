import collections
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        carry = 0
        res = collections.deque()
        while i >= 0 or j >= 0 or carry == 1:
            total = carry
            if i >= 0 and a[i] == "1":
                total += 1
            if j >= 0 and b[j] == "1":
                total += 1
            
            res.appendleft(str(total%2))
            
            carry = total // 2
            i -= 1
            j -= 1
        
        return "".join(res)


"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
