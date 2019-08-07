class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method2: sliding window
        start, end = 0, 0  # window is [start, end)
        n = len(s)
        last_appeared = {}  # {letter: index}
        longest = 0
        while start < n and end < n:
            if s[end] in last_appeared:
                longest = max(end - start, longest)
                start = max(start, last_appeared[s[end]] + 1)  # max is needed
            last_appeared[s[end]] = end
            end += 1
        longest = max(longest, end - start)  # easy to forget!
        return longest
    

        
#         # Method 1: brute force, O(n^2), Time Limit Exceeded
#         ans = 0
#         for i in range(len(s)):
#             _set = set()
#             for j in range(i, len(s)):
#                 if s[j] not in _set:
#                     _set.add(s[j])
#                 else:
#                     break
#             ans = max(ans, len(_set))
#         return ans
    
