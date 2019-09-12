import collections
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        carry = 0
        res = collections.deque()
        while i >= 0 or j >= 0 or carry == 1:
            total = carry
            if i >= 0 and a[i] == "1":
                total += 1
            if j >= 0 and b[j] == "1":
                total += 1
            
            if total % 2 == 1:
                res.appendleft("1")
            else:
                res.appendleft("0")
            
            carry = total // 2
            i -= 1
            j -= 1
        
        return "".join(res)
    
