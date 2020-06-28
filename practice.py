"""
input = " 3 + 2/5*5"
output = float


+, -, *, /
all integer in calculator
all expressions are legal
zero division: raise exception
no brackets

" 3 + 2 /5*5  "

no illegal input: " *3 + 2 /5*5  ", " *3 + 2 /5*-5  "

" 3 + 2/5*5", O(n) time/space

1. parse it, exp = " 3 + 2/5*5" => elements = [3, +, 2, /, 5, *, 5]
2. dfs to evaluate dfs(elements, i, total, pre)

arr   [3, +, 2, /, 5, *, 5]
i                            |
end                      |

"""


class Solution:
    def calculate(self, exp):
        # all legal input, but might have zero division
        elements = self.parse(exp)
        if not elements:
            return 0
        if len(elements) % 2 != 1:
            raise ValueError("input error")
        i = 0
        total = 0
        while i < len(elements):  # iteration
            end = i
            cur = int(elements[i])
            while end + 1 < len(elements) and elements[end + 1] in "/*":
                if elements[end + 1] == "/":
                    if int(elements[end + 2]) == 0:
                        raise ValueError("ZeroDivision")
                    cur /= float(elements[end + 2])
                elif elements[end + 1] == "*":
                    cur *= float(elements[end + 2])
                end += 2
            total += cur
            i = end + 2
        return total

    def parse(self, exp):
        # return a list of str
        # "- 13 + 2 / 5 * 5", " 3 + 2/5*5"  -  13  + 2  /  5  *  5
        exp = exp.replace("/", " / ")
        exp = exp.replace("*", " * ")
        exp = exp.replace("+", " + ")
        exp = exp.replace("-", " - ")
        elements = exp.split()

        if elements and elements[0] == "-":
            elements = elements[1:]
            elements[0] = "-" + elements[0]
        for i in range(1, len(elements), 2):
            if elements[i] == "-":
                elements[i] = "+"
                elements[i + 1] = "-" + elements[i + 1]
        return elements


exp = "- 13 + 2 / 5 * 5"
print(Solution().calculate(exp))
