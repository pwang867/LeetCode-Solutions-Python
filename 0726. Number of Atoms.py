# method 2, time O(n), improved space O(res)


import collections


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.defaultdict(int)]
        i = 0
        while i < len(formula):
            c = formula[i]
            if c == "(":
                stack.append(collections.defaultdict(int))
                i += 1
            elif c == ")":
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                if i > start:
                    factor = int(formula[start:i])
                    d1 = stack.pop()
                    d2 = stack[-1]
                    for el in d1:
                        d2[el] += d1[el] * factor
            elif c.isupper():
                # get name
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[start:i]
                # get count
                factor = 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                if i > start:
                    factor = int(formula[start:i])
                stack[-1][name] += factor
            else:
                i += 1
        res = []
        dic = stack[-1]
        for name in sorted(dic.keys()):
            res.append(name)
            if dic[name] > 1:
                res.append(str(dic[name]))
        return "".join(res)


# method 1, time/space O(n)


from collections import defaultdict


class Solution1(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        if not formula:
            return ""

        # parse the input
        arr = []
        for i, c in enumerate(formula):
            if c.isdigit():
                if arr and arr[-1].isdigit():
                    arr[-1] += c
                else:
                    arr.append(c)
            elif c.islower():
                arr[-1] += c
            else:
                arr.append(c)

        # merge dictionary
        stack = [defaultdict(int)]
        i = 0
        while i < len(arr):
            c = arr[i]
            if c == "(":
                stack.append(defaultdict(int))
                i += 1
            elif arr[i] == ")":
                if i + 1 < len(arr) and arr[i + 1].isdigit():
                    d = stack[-1]
                    num = int(arr[i + 1])
                    for key in d:
                        d[key] *= num
                    i += 2
                else:
                    i += 1
                if len(stack) > 1:
                    d1 = stack.pop()
                    d2 = stack[-1]
                    for key, val in d1.items():
                        d2[key] += val
            else:
                if i + 1 < len(arr) and arr[i + 1].isdigit():
                    stack[-1][c] += int(arr[i + 1])
                    i += 2
                else:
                    stack[-1][c] += 1
                    i += 1

        # product result
        d = stack[-1]
        res = []
        for key in sorted(d.keys()):
            res.append(key)
            if d[key] > 1:
                res.append(str(d[key]))

        return "".join(res)


"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters,
representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1.
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name
(in sorted order), followed by its count (if that count is more than 1),
followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""