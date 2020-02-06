# time O(n*log(n))
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ""
        res = []
        offset = ord("A")
        while n > 0:
            n, cur = divmod(n-1, 26)  # mistake: divmod(n, 26)
            res.append(chr(cur+offset))
        return "".join(res[::-1])


"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
