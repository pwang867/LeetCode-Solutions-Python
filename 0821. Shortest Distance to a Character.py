# single scan, time O(n), space O(n)
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        left, right = -float('inf'), float('inf')
        for i, c in enumerate(S):
            if c == C:
                left = i
                right = i   # can not miss this line
            elif i == 0 or S[i-1] == C:
                for j in range(i+1, len(S)):
                    if S[j] == C:
                        right = j
                        break
                else:
                    right = float('inf')
            res.append(min(i-left, right-i))
        return res


# method 2, two pass, left to right, and then right to left




"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
