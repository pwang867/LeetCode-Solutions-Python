"""
lisp
expression |= int
        | = (let var1 expr1 var2 expr2 .... expr_final) -> var1 = expr1, var2 = expr2,... return the value of expr_final
        | = (add expr1 expr2) -> return the value of expr1 + expr2

(let x 2 y (let x 4 (add x 2)) (add x y))
(let:
x = 2
y = (let x 4 (add x 2)) -> 6
return add x y -> 8
)

(let x 2 x 5 x) -> 5

evaluation(expression) -> int

(let x 2 y (let x 4 (add x 2)) (add x y))

(add 1 1)
var: no space inside

syntactically correct


(let x 2 z 3 y (let x 4 (add x z)) z 3 (add x y))

(add x y)

5 - > 5

level  + 1 - 1 find expression


(let x 10 (let x 2 x 3 z 3 y (let x 4 (add x z)) z 3 (add x y)))
            memo = [x, x, z, y]

            (let x 1 x 2.... x 10000000000 x)
            x : [1,2,3,.....100000000]

            (let x 2 x 3 (let x 4 (add x 3))
            (let vars_1[x] = 3
                (pass vars_1 into the second let scope, 
                (let vars_2[x] = 4
stack



Solution:
    vars = {x: [10], z:[3, 3], y:[]}

    evaluation(self, exp):
        # return int
        if exp is int:
            return int

        parse it as "add", exp1, exp2
        parse it as "let", var1, exp1, var2, exp2, .... , final_exp

        if exp starts with "add":

            return evaluation(exp1) + evaluation(exp2)
        elif "let":

            memo = []   # var names
            for var_i, exp_i:
                vars[var_i] = evaluate(exp_i, vars)
                memo.append(var_i)
            backtrack for vars
            return evaluation(final_exp)   

"""

import copy
import collections


class Solution:
    def evaluate(self, exp):
        return self.evaluate_helper(exp, collections.defaultdict(int))

    def add(exp1, exp2, vars):
        return self.evaluate_helpr(exp1, vars) + evalue(exp2, vars)

    def let():
        return xxx

    def evaluate_helper(self, exp, vars):
        # exp: str
        # vars: vars from top level  {x: 2}

        # input is always valid
        elements = self.parse(exp)
        # if not exp: 
        #     return 0
        if exp[0] != "(":
            return int(exp)
        if elements[0] == "add":
            return self.evaluate_helper(elements[1], vars) \
                   + self.evaluate_helper(elements[2], vars)
        elif elements[0] == "let":
            new_vars = copy.deepcopy(vars)
            n = (len(elements) - 2) // 2
            for i in range(n):
                var = elements[1 + 2 * i]
                exp = elements[2 + 2 * i]
                new_vars[var] = self.evaluate_helper(exp, new_vars)
            return self.evaluate_helper(elements[-1], new_vars)

    def parse(self, exp):
        exp = exp.strip()
        if not exp:
            return ""
        if exp[0] != "(":
            return exp
        # (let x 4 (add x z))

        stack = []
        level = 0
        start, end = 1, 1
        while end < len(exp) - 1:
            if exp[end] == "(":
                level += 1
                start = end + 1
            elif exp[end] == ")":
                level -= 1
                if level == 0:
                    stack.append(exp[start:end + 1])
                    start = end + 1
            elif exp[end] == " ":
                if level == 0:
                    stack.append(exp[start:end])
                    start = end + 1
            end += 1
        return stack

