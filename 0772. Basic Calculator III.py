# time/space O(n)
# reference: https://www.youtube.com/watch?v=C_jxn1hTn6Q


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = self.preprocess(s)
        return self.helper(queue)

    def preprocess(self, s):
        # can also add validation into this function
        queue = collections.deque([c for c in s if c != " "])
        queue.append("+")   # add dummy number to trigger the final step !!!
        queue.append("0")
        return queue

    def helper(self, queue):
        total, pre, num = 0, 0, 0
        pre_op = "+"
        while queue:
            c = queue.popleft()
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                num = self.helper(queue)
            else:  # for ")" and operators, make sure to let ")" also trigger the operations!!!
                if pre_op == "+":
                    total += pre
                    pre = num
                elif pre_op == "-":
                    total += pre
                    pre = -num
                elif pre_op == "*":
                    pre = pre * num
                elif pre_op == "/":
                    if pre < 0:
                        pre = -((-pre) // num)   # -3//2 will be -2, -(3//2) will be -1
                    else:
                        pre //= num
                num = 0
                pre_op = c
                if c == ")":
                    break
        return total + pre


"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) 
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range 
of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.
"""
