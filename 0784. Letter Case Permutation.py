# simple dfs, time/space O(res)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [""]
        res = []
        self.dfs(list(S), 0, res)
        return res
    
    def dfs(self, s, i, res):
        if i == len(s):
            res.append("".join(s))
        else:
            s[i] = s[i].lower()
            self.dfs(s, i+1, res)
            if s[i].lower() != s[i].upper():
                s[i] = s[i].upper()
                self.dfs(s, i+1, res)



"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

