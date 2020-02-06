# method 1: two pointers, modify in place
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A)-1
        
        while left < right:
            if A[left] % 2 == 0:
                left += 1
            else:
                A[left], A[right] = A[right], A[left]
                right -= 1
        
        return A
