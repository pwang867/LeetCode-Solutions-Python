# use stack, time/spaceO(n), space can be reduced to O(1)
class Solution(object):
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

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

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