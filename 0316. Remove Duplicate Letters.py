# method 2, using stack, time O(n), space O(n)
# greedy
from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        counts = Counter(s)
        stack = []    # letters in stack are unique, stack is result finally
        _set = set()  # letters in stack
        for i in range(len(s)):
            c = s[i]
            counts[c] -= 1
            if c not in _set:
                while stack and c < stack[-1] and counts[stack[-1]] > 0:
                    _set.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                _set.add(c)
        return "".join(stack)


# method 1, O(26*n), greedy, choose a smallest index i such that s[i:] 
# contains all the unique letters and s[i] is the smallest
class Solution1(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        k = len(set(s))
        visited = set()
        smallest = "z"
        p = -1   # position of the first letter of the result
        for i in range(len(s)-1, -1, -1):
            visited.add(s[i])
            if len(visited) == k and s[i] <= smallest:   
                # choose the smallest index i such that s[i:] has all the unique letters and s[i] is smallest
                smallest = s[i]
                p = i
        return s[p] + self.removeDuplicateLetters(s[p+1:].replace(s[p], ""))
    
"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
