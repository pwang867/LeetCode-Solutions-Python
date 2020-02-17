# similar to #1096, use a stack, use level-zero brackets to start a new group
import itertools
class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        stack = []
        level = 0
        for i, c in enumerate(S):
            if c == "{":
                level += 1
                stack.append([])
            elif c == "}":
                level -= 1
            elif c != ",":  # don't forget ","
                if level == 0:
                    stack.append([c])
                else:
                    stack[-1].append(c)
        
        map(lambda x: x.sort(), stack)
        return map("".join, itertools.product(*stack))
    


"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  
If there is one option, the letter is represented as is.  
If there is more than one option, then curly braces delimit the options.  
For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list 
["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

 

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
 

Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending 
curly brackets are different.
"""
