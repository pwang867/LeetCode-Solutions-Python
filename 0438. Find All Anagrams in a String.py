# sliding window + hashmap
# time O(len(s)+len(p)), space O(len(p))

import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s:
            return []
        window = collections.Counter(p)
        cnt = len(window)
        res = []
        for right, c in enumerate(s):
            if c in window:
                window[c] -= 1
                if window[c] == 0:
                    cnt -= 1
            left = right - len(p)
            if left >= 0 and s[left] in window:
                window[s[left]] += 1
                if window[s[left]] == 1:
                    cnt += 1
            if cnt == 0:
                res.append(left+1)
        return res


"""
Given a string s and a non-empty string p, 
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and 
the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

