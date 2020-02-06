# sliding window, time O(n), space O(k)
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""
