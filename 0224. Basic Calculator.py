# time/space O(n)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = self.preprocess(s)
        return self.helper(queue)

    def preprocess(self, s):
        queue = collections.deque([c for c in s if c != " "])
        queue.append("+")
        queue.append("0")
        return queue

    def helper(self, queue):
        # total + pre (pre_op) num
        if not queue:
            return 0
        total, pre, num = 0, 0, 0
        pre_op = "+"
        while queue:
            c = queue.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                num = self.helper(queue)
            else:
                if pre_op == "+":
                    total += pre
                    pre = num
                elif pre_op == "-":
                    total += pre
                    pre = -num
                if c == ")":
                    break
                num = 0
                pre_op = c
        return total + pre


"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
