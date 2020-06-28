# method 2
# sort each word and then group them into a dictionary
# time O(n*m*log(m)), n=len(strs), m=len(strs[0])


from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        
        _dict = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))   # can be optimized by counting sort if the string is very long
            _dict[temp].append(s)
        
        return _dict.values()


# method 1, counting sort

import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strs:
            key = self.get_key(s)
            d[key].append(s)
        return d.values()

    def get_key(self, s):    # use counting sort
        dic = collections.Counter(s)
        res = []
        for i in range(26):
            c = chr(i + ord('a'))
            if c in dic:
                res.append(str(dic[c]))
                res.append(c)
        return "".join(res)


"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
