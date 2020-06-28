class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0
        i = 1  # backward index
        while i <= len(a) or i <= len(b) or carry:   # mistake: i < len(a)
            if i <= len(a):
                carry += int(a[-i])
            if i <= len(b):
                carry += int(b[-i])
            res.append(str(carry & 1))   # mistake: forget str()
            carry >>= 1
            i += 1

        return "".join(res[::-1])


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
