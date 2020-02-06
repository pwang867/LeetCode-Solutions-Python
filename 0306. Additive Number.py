class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        if n < 3:
            return False
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                if self.checkNum(num, i, j):
                    return True
        
        return False
    
    def checkNum(self, num, i, j):
        if i > 0 and num[0] == "0":
            return False
        if j - i > 1 and num[i+1] == "0":
            return False
        num1, num2 = int(num[:i+1]), int(num[i+1:j+1])
        cur = j+1
        while cur < len(num):
            num3 = num1 + num2
            k = len(str(num3))
            if num[cur:cur+k] != str(num3):
                return False
            num1, num2 = num2, num3
            cur += k
        return True
    
# prune 
    
    