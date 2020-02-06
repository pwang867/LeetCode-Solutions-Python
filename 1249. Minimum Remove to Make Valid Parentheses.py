# method 2, a single pass, save index to remove
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        stack = []
        right_to_remove = []
        cnt = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                cnt += 1
            elif c == ")":
                if cnt == 0:
                    right_to_remove.append(i)
                else:
                    stack.pop()
                    cnt -= 1
        to_remove = set( right_to_remove + stack)
        res = []
        for i, c in enumerate(s):
            if i not in to_remove:
                res.append(c)
        return "".join(res)


# method 1, two pass, space/time O(n)
class Solution1(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s_list = list(s)
        s_list = self.remove(s_list, 0)
        s_list.reverse()
        s_list = self.remove(s_list, 1)
        s_list.reverse()
        return "".join(s_list)
    
    def remove(self, s_list, i):
        if not s_list:
            return []
        brackets = ["(", ")"]
        res = []
        cnt = 0
        for c in s_list:
            if c == brackets[i]:
                cnt += 1
                res.append(c)
            elif c == brackets[1-i]:
                if cnt > 0:
                    cnt -= 1
                    res.append(c)
            else:
                res.append(c)
        return res


"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""
