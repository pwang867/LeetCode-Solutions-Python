# Watch out zeros, such as 0 and 1,000,100

from collections import deque
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        res = deque()
        level = ["", "Thousand", "Million", "Billion"]
        
        order = 0
        while num > 0:
            temp = self.intToWord(num%1000)
            if temp:
                if order > 0:
                    res.appendleft(level[order])
                res.appendleft(temp)
            num = num//1000
            order += 1
        
        return " ".join(res)
    
    def intToWord(self, num):
        # 0 <= num < 1000
        # return a string
        res = []
        special = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", 
                   "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", 
                   "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", 
                "Sixty", "Seventy", "Eighty", "Ninety"]
        if num//100 > 0:
            res.append(special[num//100])
            res.append("Hundred")
            num = num%100
        if 0 < num < 20:
            res.append(special[num])
        elif num >= 20:
            res.append(tens[num//10-2])
            if num%10 != 0:
                res.append(special[num%10])
        
        return " ".join(res)
    
"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
