# sliding window, time O(n), space O(1)

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = {}    # the width of the window never decreases
        max_cnt = 0    # the max frequency that has ever appeared in the window
        left, right = 0, -1
        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            max_cnt = max(max_cnt, window[c])
            if (right-left+1) - (max_cnt+k) > 0:
                window[s[left]] -= 1
                left += 1
        return right - left + 1


"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
