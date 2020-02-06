# edge case: "abeabac", k=3
# time O(n), space O(n)
from collections import Counter
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ""
        d = Counter(s)
        arr =[(freq, c) for c, freq in d.items()]
        arr.sort(reverse=True, key=lambda x:[x[0], -ord(x[1])])
        n = arr[0][0]
        if n == 1:  # all unique
            return s
        
        res = [[] for _ in range(n)]
        i = 0
        for freq, c in arr:
            if freq == n:      # freq == n are special
                for j in range(n):
                    res[j].append(c)
                continue
            for _ in range(freq):
                res[i].append(c)
                i = (i+1)%(n-1)    # use (n-1) instead of n
        if len(res[-2]) < k:
            return ""
        return "".join(["".join(item) for item in res])

 


"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""
