# method 1
# "xyz" and "yza" are in the same group
# shift the string so that the first letter is "a" and use it as the key
from collections import defaultdict
class Solution1(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for string in strings:
            key = self.transform(string)
            d[key].append(string)
        return d.values()
    
    def transform(self, s):
        offset = ord(s[0]) - ord('a')
        res = []
        for c in s:
            num = ord(c) - offset
            if num < ord('a'):
                num += 26
            res.append(chr(num))
        return ''.join(res)



"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
