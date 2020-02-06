class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        start, end = 0, len(s)-1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
        return True


"""
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, 
we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
