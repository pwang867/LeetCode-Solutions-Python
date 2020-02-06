# edge case: "a"

# method 3: better template of sliding window
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        window = defaultdict(int)
        res = 0
        for right, c in enumerate(s):
            window[c] += 1
            while window[c] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            res = max(res, right-left+1)
        return res
    


# method 2: sliding window, record the last appeared index of all characters
# # watch out: characters saved in last_appeared might not be in the window!!!
# time/space O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0  # window is [start, end)
        n = len(s)
        last_appeared = {}  # {character: last appeared index}, 
        longest = 0
        while start < n and end < n:
            if s[end] in last_appeared:
                longest = max(end - start, longest)
                start = max(start, last_appeared[s[end]] + 1)  # max is needed
            last_appeared[s[end]] = end
            end += 1
        longest = max(longest, end - start)  # easy to forget!
        return longest

    
# Method 1: brute force, check every string starting from s[i]
# O(n^2), Time Limit Exceeded
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        ans = 0
        for i in range(len(s)):
            _set = set()
            for j in range(i, len(s)):
                if s[j] not in _set:
                    _set.add(s[j])
                else:
                    break
            ans = max(ans, len(_set))
        return ans

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "nabcabcnbb"
Output: 4 
Explanation: The answer is "abcn", with the length of 4. 
"""
