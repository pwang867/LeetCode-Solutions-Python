# we need to switch A[i] and B[i] until A or B is filled with only one common number
# the common number must be either A[0] or B[0], or other pairs (A[1], B[1])
# for each candidate, we need to consider 
# if we need to make candidates in A or make candidates in B
# so in total we have four conditions
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A:
            return 0
        if len(A) != len(B):
            return -1
        
        res = float('inf')
        
        # if the common number is A[0]
        num_rotation = self.getNumOfRotation(A, B, A[0])
        if num_rotation != -1:  # -1 means rotation is not possible
            res = min(res, num_rotation)
        
        num_rotation = self.getNumOfRotation(B, A, B[0])
        if num_rotation != -1:
            res = min(res, num_rotation)
        
        return res if res != float('inf') else -1
    
    def getNumOfRotation(self, A, B, candidate):
        cntA, cntB = 0, 0
        for i in range(len(A)):  # corner case: A[i] == B[i] == candidate
            if A[i] == candidate:
                cntA += 1
            if B[i] == candidate:
                cntB += 1
            if A[i] != candidate and B[i] != candidate:
                return -1
        
        # the candidate may be aligned in the upper or lower row
        return min(len(A)-cntA, len(A)-cntB)  
    
