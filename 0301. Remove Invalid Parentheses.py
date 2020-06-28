# time/space O(res)
# the solution below will use a lot of early termination
# we can guarantee the final answer will be correct, but there will still have some waste in the middle,
# such as for case (())(, we will still have a branch deleting the first "("


class Solution1(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left_del, right_del = 0, 0  # left_del means number of "(" to delete
        left_total = 0
        for i, c in enumerate(s):
            if c == "(":
                left_del += 1
                left_total += 1
            elif c == ")":
                if left_del == 0:
                    right_del += 1
                else:
                    left_del -= 1
        # mistake (forget letters): left_add = right_add = (len(s) - left_del - right_del)//2
        left_add = right_add = left_total - left_del  # left_add means number of "(" to add
        res = []
        self.dfs(s, 0, left_del, right_del, left_add, right_add, False, [], res)
        return res

    def dfs(self, s, i, left_del, right_del, left_add, right_add,
            pre_del, path, res):
        # pre_del means if the previous "(" is deleted. For "((())", we will only try deleting the first "("
        if i == len(s):
            res.append("".join(path))
            return
        if s[i] == "(":
            if left_add > 0:
                path.append("(")
                self.dfs(s, i + 1, left_del, right_del, left_add - 1,
                         right_add, False, path, res)
                path.pop()
            if left_del > 0 and (i == 0 or s[i] != s[i - 1] or pre_del):  # avoid duplicate for cases like "(((a)"
                self.dfs(s, i + 1, left_del - 1, right_del, left_add,
                         right_add, True, path, res)
        elif s[i] == ")":
            if right_add > left_add:
                path.append(")")
                self.dfs(s, i + 1, left_del, right_del, left_add,
                         right_add - 1, False, path, res)
                path.pop()
            if right_del > 0 and (i == 0 or s[i] != s[i - 1] or pre_del):
                self.dfs(s, i + 1, left_del, right_del - 1, left_add,
                         right_add, True, path, res)
        else:
            path.append(s[i])
            self.dfs(s, i + 1, left_del, right_del, left_add,
                     right_add, False, path, res)
            path.pop()


"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
    
