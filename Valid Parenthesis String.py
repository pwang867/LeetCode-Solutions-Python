# method 3, optimal, time O(n), space O(1)
# optimized from iterative dp
# min_cnt, max_cnt are the minimum and maximum counts of leftover "("
# range(min_cnt, max_cnt+1) are all possible, so we don't need to save all of them
# only need to save the lower and upper bound


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_cnt, max_cnt = 0, 0  # count of possible leftover "(" so far
        for i, c in enumerate(s):
            if c == "(":
                min_cnt += 1
                max_cnt += 1
            elif c == ")":
                if max_cnt == 0:
                    return False
                min_cnt = max(0, min_cnt - 1)
                max_cnt -= 1
            else:
                min_cnt = max(0, min_cnt - 1)
                max_cnt += 1
        return min_cnt <= 0 <= max_cnt


# method 2, dp, O(n^2), space O(n)




# method 1, time O(n^2), space O(n)

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dp = {0}
        for i, c in enumerate(s):
            new_dp = set()
            for num_left in dp:
                if c == "(":
                    new_dp.add(num_left + 1)
                elif c == ")":
                    if num_left - 1 >= 0:
                        new_dp.add(num_left - 1)
                else:
                    new_dp.add(num_left)
                    new_dp.add(num_left + 1)
                    if num_left - 1 >= 0:
                        new_dp.add(num_left - 1)
            dp = new_dp
        return 0 in dp


# time/space O(n^2)


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.dfs(s, 0, 0, {})

    def dfs(self, s, i, left, memo):
        # return whether s[i:] can form a valid parenthesis when there are left "(" to its left
        if left < 0:
            return False
        if i == len(s):
            return left == 0
        if (i, left) in memo:
            return memo[(i, left)]
        res = False
        if s[i] == "(":
            res = self.dfs(s, i + 1, left + 1, memo)
        elif s[i] == ")":
            res = self.dfs(s, i + 1, left - 1, memo)
        else:
            res = self.dfs(s, i + 1, left + 1, memo) or self.dfs(s, i + 1, left - 1, memo) \
                  or self.dfs(s, i + 1, left, memo)
        memo[(i, left)] = res
        return res


"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""