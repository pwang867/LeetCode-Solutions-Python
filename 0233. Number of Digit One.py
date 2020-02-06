"""
The idea is to calculate occurrence of 1 on every digit. There are 3 scenarios, for example

if n = xyzdabc
and we are considering the occurrence of one on thousand, it should be:

(1) xyz * 1000 + 0                if d == 0, means there is no 1 because of  this digit(none)
(2) xyz * 1000 + abc + 1          if d == 1, means there is abc of  1 because  of this digit(patrial)
(3) xyz * 1000 + 1000             if d > 1,  means there  is fully 1000 of  1 because of  this digit(fully)
"""



class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """





"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
