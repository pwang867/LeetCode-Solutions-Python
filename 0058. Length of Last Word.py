# we can also use s.rstrip() and s.split(), but will use O(n) space



# time O(len(last_word)), space O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        end = len(s)-1
        see_letter = False
        for start in range(len(s)-1, -1, -1):
            if s[start] == " ":
                if not see_letter:
                    end -= 1
                else:
                    return end - start
            else:
                see_letter = True
        
        return end + 1 if see_letter else 0

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
