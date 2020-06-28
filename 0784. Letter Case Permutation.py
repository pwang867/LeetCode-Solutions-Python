# simple dfs, time/space O(res)


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        arr = list(S.lower())
        res = []
        self.dfs(arr, 0, res)
        return res

    def dfs(self, arr, start, res):
        if start == len(arr):
            res.append("".join(arr))
            return
        self.dfs(arr, start + 1, res)
        if arr[start].isalpha():
            arr[start] = arr[start].upper()
            self.dfs(arr, start + 1, res)
            arr[start] = arr[start].lower()


"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

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

