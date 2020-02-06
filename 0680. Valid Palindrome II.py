class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return True
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return self.isPalindrome(s, i, n-2-i) or self.isPalindrome(s, i+1, n-1-i)
        return True
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
