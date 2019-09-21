# use stack to save left brackets,
# pop the stack once we see a paired right bracket
# time O(n), space O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
    
