# time/space O((n/2)!)
import collections
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = collections.Counter(s)
        center = ""
        temp = []  # candidates for left half of palindromes
        for key, val in d.items():
            if val%2 == 1:
                if center == "":
                    center = key
                else:
                    return []
            temp.append(key*(val//2))
        _str = "".join(temp)
        
        left_halves = []
        self.permutations(_str, "", left_halves)
        
        return [left + center + left[::-1] for left in left_halves]
    
    def permutations(self, s, path, res):
        # get all permutations of s, save to res
        if not s:
            res.append(path)
            return
        
        for i, c in enumerate(s):
            if i > 0 and s[i] == s[i-1]:  # skip duplicates
                continue
            self.permutations(s[:i]+s[i+1:], path+c, res)

"""
Given a string s, return all the palindromic permutations (without duplicates) 
of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
"""
