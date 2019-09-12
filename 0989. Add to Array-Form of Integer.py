class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        res = []
        i = len(A)-1
        carry = 0
        
        while i >= 0 or K > 0 or carry > 0:
            
            num1 = A[i] if i >= 0 else 0  
            num2 = K%10
            cur = num1 + num2 + carry  # don't forget carry
            res.append(cur%10)
            
            carry = cur//10  # update all three variables
            i -= 1
            K /= 10
        
        return res[::-1]
    
