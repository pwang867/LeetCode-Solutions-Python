# time O(n), space O(1)
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        window = defaultdict(int)
        res = 0
        left = 0
        for right, c in enumerate(s):
            window[c] += 1
            while len(window) > 2:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            res = max(res, right-left+1)
        return res
    


"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
