# improve readability


import copy
import collections


class Solution:
    def evaluate(self, exp):
        return self.evaluate_helper(exp, collections.defaultdict(int))

    def add(self, exp1, exp2, vars):
        return self.evaluate_helper(exp1, vars) + self.evaluate_helper(exp2, vars)

    def mult(self, exp1, exp2, vars):
        return self.evaluate_helper(exp1, vars) * self.evaluate_helper(exp2, vars)

    def let(self, elements, vars):
        new_vars = copy.deepcopy(vars)
        n = (len(elements) - 2) // 2
        for i in range(n):
            var = elements[1 + 2 * i]
            exp = elements[2 + 2 * i]
            new_vars[var] = self.evaluate_helper(exp, new_vars)
        return self.evaluate_helper(elements[-1], new_vars)

    def evaluate_helper(self, exp, vars):
        # input is always valid
        # if not exp:
        #     return 0
        elements = self.parse(exp)
        if len(elements) == 1:
            x = elements[0]
            if x.isdigit() or (x[0] in "-+" and x[1:].isdigit()):
                return int(x)
            else:
                return vars[x]
        if elements[0] == "add":
            return self.add(elements[1], elements[2], vars)
        elif elements[0] == "mult":
            return self.mult(elements[1], elements[2], vars)
        elif elements[0] == "let":
            return self.let(elements, vars)

    def parse(self, exp):
        exp = exp.strip()
        if not exp:
            return []
        if exp[0] != "(":
            return [exp]
        stack = []
        start = 1
        while start < len(exp) - 1:
            c = exp[start]
            if c == "(":
                level = 0
                end = start
                while end < len(exp) - 1:
                    if exp[end] == "(":
                        level += 1
                    elif exp[end] == ")":
                        level -= 1
                    if level == 0:
                        break
                    end += 1
                stack.append(exp[start:end + 1])
                start = end + 1
            elif c != " ":
                end = start
                while end < len(exp) - 1 and exp[end] != " ":
                    end += 1
                stack.append(exp[start:end])
                start = end
            else:
                start += 1
        return stack


class Solution1:
    def evaluate(self, exp):
        return self.evaluate_helper(exp, collections.defaultdict(int))

    def add(self, exp1, exp2, vars):
        return self.evaluate_helper(exp1, vars) + self.evaluate_helper(exp2, vars)

    def mult(self, exp1, exp2, vars):
        return self.evaluate_helper(exp1, vars) * self.evaluate_helper(exp2, vars)

    def let(self, elements, vars):
        new_vars = copy.deepcopy(vars)
        n = (len(elements) - 2) // 2
        for i in range(n):
            var = elements[1 + 2 * i]
            exp = elements[2 + 2 * i]
            new_vars[var] = self.evaluate_helper(exp, new_vars)
        return self.evaluate_helper(elements[-1], new_vars)

    def evaluate_helper(self, exp, vars):
        # input is always valid
        # if not exp:
        #     return 0
        elements = self.parse(exp)
        if len(elements) == 1:
            x = elements[0]
            if x.isdigit() or (x[0] in "-+" and x[1:].isdigit()):
                return int(x)
            else:
                return vars[x]
        if elements[0] == "add":
            return self.add(elements[1], elements[2], vars)
        elif elements[0] == "mult":
            return self.mult(elements[1], elements[2], vars)
        elif elements[0] == "let":
            return self.let(elements, vars)

    def parse(self, exp):
        exp = exp.strip()
        if not exp:
            return []
        if exp[0] != "(":
            return [exp]
        stack = []
        level = 0
        start, end = 1, 1
        while end < len(exp) - 1:
            if exp[end] == "(":
                level += 1
                if level == 1:
                    start = end
            elif exp[end] == ")":
                level -= 1
                if level == 0:
                    stack.append(exp[start:end + 1])
                    start = end + 1
            elif exp[end] == " ":
                if level == 0:
                    if start < end:
                        stack.append(exp[start:end])
                    start = end + 1
            else:
                if end == len(exp) - 2:
                    stack.append(exp[start:end + 1])
            end += 1
        return stack


# time O(n)


class Solution1(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        expression = expression.replace("(", " ( ").replace(")", " ) ")
        arr = collections.deque(expression.split())
        dic = collections.defaultdict(list)

        def eval(arr):
            # evaluate the leftmost expression in arr
            # remove it from arr, and return the value
            if not arr:
                return 0
            elif arr[0].isdigit() or arr[0][0] == "-":
                return int(arr.popleft())
            elif arr[0][0].isalpha():   # last of let expression
                var = arr.popleft()
                return dic[var][-1]
            else:
                arr.popleft()  # remove "("
                key = arr.popleft()
                if key == "add":
                    val = eval(arr) + eval(arr)
                    arr.popleft()  # remove ")"
                    return val
                elif key == "mult":
                    val = eval(arr) * eval(arr)
                    arr.popleft()
                    return val
                else:  # "let"
                    temp_vars = []
                    while arr:
                        if arr[0] == "(" or arr[1] == ")":
                            # when we reach the last expression of let-exp
                            val = eval(arr)
                            arr.popleft()
                            # clean up the temporary variables in current level
                            while temp_vars:
                                var = temp_vars.pop()
                                dic[var].pop()
                            return val
                        else:
                            var = arr.popleft()
                            val = eval(arr)
                            dic[var].append(val)
                            temp_vars.append(var)

        return eval(arr)


"""
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. 
Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then 
there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned 
the value of the expression e1, the second variable v2 is assigned the value of the expression e2, 
and so on sequentially; 
and then the value of this let-expression is the value of the expression expr.
An add-expression takes the form (add e1 e2) where add is always the string "add", there are always 
two expressions e1, e2, 
and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always 
two expressions e1, e2, 
and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a 
lowercase letter, 
then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are 
protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that 
evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then 
outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for 
more details on scope.
Evaluation Examples:
Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.

Note:

The given string expression is well formatted: There are no leading or trailing spaces, 
there is only a single space separating different components of the string, and no space between adjacent parentheses. 
The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
"""

