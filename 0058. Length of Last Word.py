# we can also use s.rstrip() and s.split(), but will use O(n) space


# time O(len(last_word)), space O(1)


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = len(s) - 1
        while end >= 0 and not s[end].isalpha():
            end -= 1
        cnt = 0
        while end >= 0 and s[end].isalpha():
            end -= 1
            cnt += 1
        return cnt


"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
