# there are only 2^26 paths at most
# time/space O(2^26), and use bitmask

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # don't forget: if len(word) == len(set(word))
        arr = list(set([self.word2mask(word) for word in arr  \
                if len(word)==len(set(word))]))
        dp = {0}   # mistake: dp = set()
        for mask in arr:
            new_dp = set()
            for x in dp:
                if (x & mask):
                    continue
                new_dp.add(x|mask)
            dp |= new_dp
        res = 0
        for x in dp:
            res = max(res, bin(x).count('1'))
        return res
    
    def word2mask(self, word):
        mask = 0
        for c in word:
            mask |= (1<<ord(c)-ord('a'))
        return mask


# method 1, brute force, time O(2^n), space O(len(arr))

class Solution1(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        arr = [s for s in arr if len(set(s))==len(s)]
        self.res = 0
        self.dfs(arr, 0, set())
        return self.res
    
    def dfs(self, arr, start, path):
        self.res = max(self.res, len(path))
        for i in range(start, len(arr)):
            s = set(arr[i])
            if not (s & path):
                self.dfs(arr, i+1, s|path)


"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
