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
            temp = "".join(sorted(s))
            _dict[temp].append(s)
        
        return _dict.values()


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
