# method 2, use the same method that works for calculator I, II, and III
# tiem/space O(n)

class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = self.preprocess(s)
        total, pre, num = 0, 0, 0
        pre_op = "+"
        while queue:
            c = queue.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if pre_op == "+":
                    total += pre
                    pre = num
                elif pre_op == "-":
                    total += pre
                    pre = -num
                elif pre_op == "*":
                    pre *= num
                elif pre_op == "/":
                    pre = pre // num if pre >= 0 else -((-pre) // num)     # in python, -3//2 = -2, -(3//2) = -1
                pre_op = c
                num = 0
        return total + pre

    def preprocess(self, s):
        queue = collections.deque([c for c in s if c != " "])
        queue.append("+")
        queue.append("0")
        return queue


# method 3, optimized from method 2, time O(n), space O(1)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total, pre, num = 0, 0, 0
        pre_op = "+"
        i = 0
        while i <= len(s):   # we need i == len(s) to trigger the last step
            if i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
            elif i == len(s) or s[i] in "+-*/":
                if pre_op == "+":
                    total += pre
                    pre = num
                elif pre_op == "-":
                    total += pre
                    pre = -num
                elif pre_op == "*":
                    pre *= num
                elif pre_op == "/":
                    pre = pre // num if pre >= 0 else -((-pre) // num)
                if i < len(s):
                    pre_op = s[i]
                    num = 0
            i += 1
        return total + pre


# method 1, use stack, time/spaceO(n), space can be reduced to O(1)


class Solution1(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            
            if c in "+-*/":
                i += 1
                start = i
                while i < len(s) and (s[i].isdigit() or s[i]==" "):  
                    # find number after operator
                    i += 1
                num = int(s[start:i])
                if c == "+":
                    stack.append(num)
                elif c == "-":
                    stack.append(-num)
                elif c == "*":
                    stack[-1] *= num
                else:
                    stack[-1] = stack[-1]/num if stack[-1] >= 0 else -(abs(stack[-1])/num)
            elif c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                stack.append(num)
            else:
                i += 1
            
        return sum(stack)


"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
Accepted
"""
