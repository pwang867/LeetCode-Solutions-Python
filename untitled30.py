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
    