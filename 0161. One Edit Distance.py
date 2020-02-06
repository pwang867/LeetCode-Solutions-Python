# similar questions: 72. Edit distance

# s and t can not be equal
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False  # edge case
        
        m, n = len(s), len(t)
        if m == n:
            flag = 0  # replace
        elif m - n == 1:
            flag = 1  # delete
        elif m - n == -1:
            flag = -1  # insert
        else:
            return False
        edited = False
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if edited:
                    return False
                if flag == 0:
                    i += 1
                    j += 1
                elif flag == 1:
                    i += 1
                else:
                    j += 1
                edited = True
        
        return True

"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""
