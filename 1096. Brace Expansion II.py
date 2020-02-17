# main idea: partition expression by level-zero "," and level-zero "{}"

# stack = [group1, group2], groups are separated by level=0 ",", 
# groups will be unioned
# group1 = [elment1, element2], elements are separated by level=0 "{}" 
# or being a single letter, elements will be producted
# "ab, {c, d}, e{f,g}{h,i}" will be expressed as 
# [[[a],[b]],  [[c,d]],   [[e],[f,g],[h,i]]]

import itertools
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = [[]]
        level = 0  # to help find the outmost pair of {}
        start = 0  # the first index of outmost pair {}
        for i, c in enumerate(expression):
            if c == "{":
                level += 1
                if level == 1:  # start a new element
                    start = i+1
            elif c == "}":  
                level -= 1
                if level == 0:  # finish an element
                    stack[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ",":  # start a new group
                if level == 0:  # easy to forget this conditionlevel == 0
                    stack.append([])
            else:  # for letter
                if level == 0:  # easy to forget
                    stack[-1].append([c])  # wrong: stack[-1].append(c)
        
        res = set()
        for group in stack:
            s = itertools.product(*group)
            s = map("".join, s)
            res = res.union(set(s))
            
        return sorted(res)



    
"""
Under a grammar given below, strings can represent a set of lowercase words.  
Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions, 
we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains 
each word at most once)
When we concatenate two expressions, we take the set of possible 
concatenations between two words where the first word comes from the first 
expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", 
"acdfh", "acefg", "acefh"}
Formally, the 3 rules for our grammar:

For every lowercase letter x, we have R(x) = {x}
For expressions e_1, e_2, ... , e_k with k >= 2, 
we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
For expressions e_1 and e_2, we have R(e_1 + e_2) = 
{a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes concatenation, 
and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, 
return the sorted list of words that the expression represents.

 

Example 1:

Input: "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
"""
