# method 3, brilliant method from lee215
# worm hole, time/space O(n)
# ref: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/383670/
# JavaC%2B%2BPython-Why-not-O(N)


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # link '(' and ')'
        stack = []
        pairs = {}
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i
        # move in worm holes
        i = 0
        d = 1  # direction of moving
        res = []
        while i < len(s):
            if s[i] in "()":
                i = pairs[i]   # most important two lines of codes
                d = -d         # jump to its pair and change direction
            else:
                res.append(s[i])
            i += d
        return "".join(res)
    

# method 2, time O(n^2), space O(n), use stack


class Solution2(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[]]
        for i, c in enumerate(s):
            if c == "(":
                stack.append([])
            elif c == ")":
                stack[-1].reverse()
                if len(stack) > 1:
                    last = stack.pop()
                    stack[-1] += last
            else:
                stack[-1].append(c)
        return "".join(stack[-1])
    


# time complexity: O(n^2), record the level of brackets
class Solution1(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        stack = []
        order = 1
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append((s[start:i], order))
                order += 1
                start = i + 1
            elif c == ")":
                stack.append((s[start:i], order))
                self.merge(stack)
                stack[-1] = (stack[-1][0][::-1], order-1)
                order -= 1
                start = i + 1
        stack.append((s[start:], order))
        return "".join([x[0] for x in stack])

    def merge(self, stack):
        while len(stack) > 1:
            if stack[-1][1] == stack[-2][1]:
                temp = stack.pop()[0]
                stack[-1] = (stack[-1][0]+temp, stack[-1][1])
            else:
                break


if __name__ == "__main__":
    s = "a(bcdefghijkl(mno)p)q"
    print(Solution().reverseParentheses(s))
    print("apmnolkjihgfedcbq")


"""
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""
