# sliding window + hashmap
# time O(len(s)+len(p)), space O(len(p))
from collections import Counter, defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = Counter(p)
        
        cnt = 0
        left = 0
        window = defaultdict(int)
        res = []
        for i, c in enumerate(s):
            if c not in target:
                window.clear()
                left = i + 1
                cnt = 0
            else:
                window[c] += 1
                if window[c] <= target[c]:
                    cnt += 1
                else:
                    while window[c] > target[c]:
                        window[s[left]] -= 1
                        if window[s[left]] < target[s[left]]:
                            cnt -= 1
                        left += 1
                if cnt == len(p):  # mistake: if cnt == 0
                    res.append(i-len(p)+1)
        
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

