# greedy approach, time/space O(n)
# same as problem #316


class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        cnts = collections.Counter(text)
        stack = []   # elements in stack will be used and matches with visited, O(26) = O(1)
        visited = set()
        for c in text:
            cnts[c] -= 1
            if c in visited:  # must do it before while loop, edge case: abcacb
                continue
            while stack and stack[-1] > c and cnts[stack[-1]] > 0:
                tmp = stack.pop()
                visited.remove(tmp)
            visited.add(c)
            stack.append(c)
        return "".join(stack)


"""
Return the lexicographically smallest subsequence of text that contains all 
the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"
 

Constraints:

1 <= text.length <= 1000
text consists of lowercase English letters.
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""
