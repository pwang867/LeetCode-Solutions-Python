import collections
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = collections.deque()
        
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            cur = carry
            if i >= 0:
                cur += int(num1[i])
            if j >= 0:
                cur += int(num2[j])
            
            carry = cur//10
            res.appendleft(str(cur%10))
            
            i -= 1
            j -= 1
        
        return ''.join(res)
    
