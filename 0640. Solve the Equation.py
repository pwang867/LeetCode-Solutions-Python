class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left_exp, right_exp = equation.split("=")
        left_cnt_x, left_sum = self.simplify(left_exp)
        right_cnt_x, right_sum = self.simplify(right_exp)
        cnt_x = left_cnt_x - right_cnt_x
        total_sum = right_sum - left_sum
        if cnt_x == 0:
            if total_sum == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(total_sum // cnt_x)

    def simplify(self, exp):
        arr = self.parse(exp)
        cnt_x = 0
        total = 0
        i = 0
        if arr[0] not in ["+", "-"]:
            i += 1
            if arr[0].isdigit():
                total += int(arr[0])
            else:
                cnt_x += self.get_coeff(arr[0])
        while i < len(arr):
            op = arr[i]
            s = arr[i + 1]
            if op == "+":
                if s.isdigit():
                    total += int(s)
                else:
                    cnt_x += self.get_coeff(s)
            else:
                if s.isdigit():
                    total -= int(s)
                else:
                    cnt_x -= self.get_coeff(s)
            i += 2
        return (cnt_x, total)

    def parse(self, exp):
        exp = exp.replace("+", " + ")
        exp = exp.replace("-", " - ")
        arr = exp.split()
        return arr

    def get_coeff(self, s):
        if s == "x":
            return 1
        return int(s[:-1])


"""
Solve a given equation and return the value of x in the form of string "x=#value". 
The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""
