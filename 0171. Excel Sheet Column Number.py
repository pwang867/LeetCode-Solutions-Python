class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str, 
        s must be capital
        :rtype: int
        """
        ans = 0
        offset = ord("A")
        for i in range(len(s)):
            ans = ans*26 + ord(s[i]) - offset + 1
        
        return ans
    


"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
