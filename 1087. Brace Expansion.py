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
    
