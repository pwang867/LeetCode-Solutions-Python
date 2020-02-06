# KMP algorithm, worst time O(n+m), space O(m), m=len(needle)
class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        table = self.getTable(needle)   # create KMP lookup table
        
        j = 0  # pointer in needle
        for i in range(len(haystack)):
            while j > 0 and needle[j] != haystack[i]:  # similar to the lines in getTable()
                j = table[j-1]
            if needle[j] == haystack[i]:
                j += 1
                if j == len(needle):
                    return i - len(needle) + 1
        
        return -1
    
    def getTable(self, needle):
        # create a KMP lookup table for the str pattern of needle
        # table[i] means the max length of same prefix and suffix in needle[:i+1]
        table = [0]*len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = table[j-1]
            if needle[j] == needle[i]:
                j += 1
            table[i] = j
        return table


# brute force, time O(m*n), space O(1)
class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        m = len(haystack)
        n = len(needle)
        
        # take out a block of n from haystack and compare with needle
        for i in range(m-n + 1):
            block = haystack[i: i+n]
            if block == needle:
                return i
        
        return -1

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
    