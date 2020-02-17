# straightforward, O(n)
# "a" is larger than 'A' by 32

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str,
        :rtype: str
        """
        res = []
        for c in str:
            if 0 <= ord(c) - ord('A') <= 25:
                res.append(chr(ord(c) + 32))  # "a" is larger than 'A' by 32
            else:
                res.append(c)  # input str may contain lower letter
        return "".join(res)
    
"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""
