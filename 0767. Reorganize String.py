import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        cnts = collections.Counter(S)
        max_cnt = max(cnts.values())
        if max_cnt > sum(cnts.values()) - max_cnt + 1:
            return ""
        res = [[] for _ in range(max_cnt)]
        for c, cnt in cnts.items():
            if cnt == max_cnt:
                for i in range(max_cnt):
                    res[i].append(c)
        j = 0
        for c, cnt in cnts.items():
            if cnt != max_cnt:
                for _ in range(cnt):
                    res[j].append(c)
                    j = (j+1)%max_cnt
        return "".join(map(''.join, res))


"""
Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
