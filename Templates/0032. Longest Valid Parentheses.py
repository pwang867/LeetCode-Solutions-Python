# method 1: dp, p[i] means the length of the longest valid parentheses ending in s[i]


class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        dp = [0] * len(s)

        if s[0] == "(" and s[1] == ")":
            dp[1] = 2

        for i in range(2, len(s)):
            if i - 1 - dp[i - 1] >= 0 and s[i] == ")" and s[i - 1 - dp[i - 1]] == "(":
                dp[i] = 2 + dp[i - 1]
                if i - 2 - dp[i - 1] >= 0:  # this if clause must be inside the first if clause!
                    dp[i] += dp[i - 2 - dp[i - 1]]

        return max(dp)


# dp, time/space O(n)
# method 3: dp[i] means the length of the longest valid parentheses ending in s[i]
# method 3: dp, simplified from method 1 by using padding


class Solution3(object):
    def longestValidParentheses(self, s):
        s = "##" + s  # use padding, consumes extra O(n) space 
        dp = [0]*len(s)
        
        res = 0
        for i in range(2, len(s)):
            if s[i] == ")" and s[i-1-dp[i-1]] == "(":
                # easy to forget: + dp[i-2-dp[i-1]]
                dp[i] = 2 + dp[i-1] + dp[i-2-dp[i-1]]  
            res = max(res, dp[i])
        
        return res


# stack, time/space O(n)


class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        last_bad_right = -1
        max_len = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if not stack:
                    last_bad_right = i
                else:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - last_bad_right)
        return max_len



"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses 
substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
