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
    
