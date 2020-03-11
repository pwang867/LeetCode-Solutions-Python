# stack, and greedy, always add a bracket right next to the invalid one
# time O(N), space O(1)
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        invalid_left = 0  # like a stack
        invalid_right = 0
        for c in S:
            if c == "(":
                invalid_left += 1
            else:
                if invalid_left > 0:
                    invalid_left -= 1
                else:
                    invalid_right += 1
        return invalid_left + invalid_right


# simple stack, with greedy, time/space O(N)
class Solution1(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []  # only save invalid left brackets
        invalid_right = 0
        for c in S:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    invalid_right += 1
        return invalid_right + len(stack)


"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.
"""