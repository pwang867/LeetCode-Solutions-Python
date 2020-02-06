# this problem is a post-order traversal of the expression tree

# method 2: we can also scan forward


# method 1: scan backwards, time O(n), space O(n)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)-1, -1, -1):
            token = tokens[i]
            stack.append(token)
            while len(stack) >= 3 and not self.isOp(stack[-1]) \
            and not self.isOp(stack[-2]) and self.isOp(stack[-3]):
                x = stack.pop()
                y = stack.pop()
                op = stack.pop()
                temp = self.evaluate(x, y, op)
                stack.append(temp)
        return stack[0]
    
    def isOp(self, s):
        if s in ["+", "-", "*", "/"]:
            return True
        else:
            return False
    
    def evaluate(self, x, y, op):
        x, y = int(x), int(y)
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            if x*y >= 0:
                return abs(x)//abs(y)
            else:
                return -(abs(x)//abs(y))   # truncate towards 0
        else:
            raise ValueError("not recognized operator")


"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
"""

