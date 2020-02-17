# method 1: produce representation directly from Roman definition
from collections import deque
class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int, 1~3999
        :rtype: str
        """
        # check input
        if num < 1 or num > 3999:
            raise ValueError("wrong input")
        
        # to make this funciton transferrable
        roman = ("I", "V", "X", "L", "C", "D", "M")
        
        res = deque()
        level = 0  # indicator for the digit weight
        while (num > 0):
            digit = num%10
            num = num//10
            if digit < 4:
                res.appendleft(roman[level]*digit)
            elif digit == 4:
                res.appendleft(roman[level] + roman[level + 1])
            elif digit <= 8:  # mistake: digit < 8
                res.appendleft(roman[level + 1] + roman[level]*(digit - 5))
            elif digit == 9:
                res.appendleft(roman[level] + roman[level + 2])
            level += 2
        
        return "".join(res)


# method 2
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [(1000, "M"), 
                 (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                 (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), 
                 (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        i = 0
        res = []
        
        while num > 0:
            if (num < roman[i][0]):
                i += 1
            else:
                num -= roman[i][0]
                res.append(roman[i][1])
        
        return "".join(res)



"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

"""