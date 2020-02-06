# number of letters in s appearing odd times should be no more than once
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = Counter(list(s))
        odd_cnt = 0
        for value in d.values():
            if value%2 == 1:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        return True


"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
